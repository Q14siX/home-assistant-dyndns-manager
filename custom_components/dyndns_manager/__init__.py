from __future__ import annotations

import logging
import ipaddress
import importlib
from datetime import datetime, timezone
from aiohttp import web, BasicAuth

from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.components.http import HomeAssistantView
from homeassistant.helpers.dispatcher import async_dispatcher_send

from .const import (
    DOMAIN, CONF_PROVIDER, CONF_DOMAINS, CONF_WEB_USER, CONF_WEB_PASS,
    UPDATE_PATH, SIGNAL_DOMAINS_UPDATED, SIGNAL_RESULTS_UPDATED,
)

PLATFORMS = [Platform.SENSOR, Platform.BUTTON]

_LOGGER = logging.getLogger(__name__)

async def _svc(hass: HomeAssistant):
    """Lazy-Import von services.py ohne den Event-Loop zu blockieren."""
    return await hass.async_add_executor_job(importlib.import_module, ".services", __package__)


async def async_setup(hass: HomeAssistant, config: dict):
    return True


def _merged_entry_data(entry: ConfigEntry) -> dict:
    merged = dict(entry.data)
    merged.update(entry.options or {})
    return merged


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    hass.data.setdefault(DOMAIN, {})
    merged = _merged_entry_data(entry)
    hass.data[DOMAIN][entry.entry_id] = {
        "domains": merged.get(CONF_DOMAINS, []),
        "provider": merged.get(CONF_PROVIDER),
        "web_user": merged.get(CONF_WEB_USER),
        "web_pass": merged.get(CONF_WEB_PASS),
        "last_results": {},
    }

    # Services einmalig registrieren (non-blocking Lazy-Import)
    if not hass.data[DOMAIN].get("_services_registered"):
        services_mod = await _svc(hass)
        await services_mod.async_setup_services(hass)
        hass.data[DOMAIN]["_services_registered"] = True

    async def _options_updated(hass_: HomeAssistant, updated_entry: ConfigEntry):
        data = hass.data[DOMAIN][updated_entry.entry_id]
        merged2 = _merged_entry_data(updated_entry)
        data["domains"] = merged2.get(CONF_DOMAINS, [])
        data["web_user"] = merged2.get(CONF_WEB_USER)
        data["web_pass"] = merged2.get(CONF_WEB_PASS)
        async_dispatcher_send(hass, SIGNAL_DOMAINS_UPDATED, updated_entry.entry_id, list(data["domains"]))

    entry.async_on_unload(entry.add_update_listener(_options_updated))

    # View nur einmal registrieren (global für alle Einträge)
    if not hass.data[DOMAIN].get("_view_registered"):
        hass.http.register_view(DynDNSUpdateView(hass))
        hass.data[DOMAIN]["_view_registered"] = True

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id, None)

        # Nur echte Entry-Keys zählen (Flags wie "_services_registered" ignorieren)
        remaining_entries = [k for k in hass.data[DOMAIN].keys() if not k.startswith("_")]

        if not remaining_entries:
            services_mod = await _svc(hass)
            await services_mod.async_unload_services(hass)
            hass.data.pop(DOMAIN, None)
    return unload_ok


def _classify_ip(ip: str | None):
    if not ip:
        return None
    try:
        addr = ip.strip()
        ipaddress.ip_address(addr)
        return "v6" if ":" in addr else "v4"
    except Exception:
        return None


# --- BEGIN: Severity handling ---

_DYNDNS2_SEVERITY = {
    # DynDNS2 Standard
    "badauth": 100,
    "911": 90,
    "abuse": 80,
    "badagent": 70,
    "notfqdn": 60,
    "nohost": 50,
    "numhost": 40,
    "dnserr": 35,
    "nochg": 10,
    "good": 0,

    # HTTP/Transport
    "http429": 85,
    "http403": 80,
    "http401": 80,
    "http5xx": 75,
    "http4xx": 60,
    "neterr": 70,
}

def _normalize_reply(code_raw: str | None) -> str:
    if not code_raw:
        return "911"

    code = code_raw.strip()
    token = code.split()[0].lower() if code else ""

    # DuckDNS
    duck = code.upper()
    if duck == "OK":
        return "good"
    if duck.startswith("KO:WRONGTOKEN") or duck == "KO":
        return "badauth"
    if duck == "TOO_MANY_UPDATES":
        return "http429"
    if duck.startswith("KO:DOMAIN"):
        return "nohost"

    # HTTP Status
    if token.isdigit() and len(token) == 3:
        n = int(token)
        if n == 401:
            return "http401"
        if n == 403:
            return "http403"
        if n == 429:
            return "http429"
        if 500 <= n <= 599:
            return "http5xx"
        if 400 <= n <= 499:
            return "http4xx"
        if 200 <= n <= 299:
            return "good"

    # Textbasierte Fehler
    low = code.lower()
    if "rate" in low and ("limit" in low or "limited" in low):
        return "http429"
    if "timeout" in low or "timed out" in low or "connection" in low:
        return "neterr"
    if "forbidden" in low:
        return "http403"
    if "unauthorized" in low:
        return "http401"
    if "server error" in low or "internal error" in low:
        return "http5xx"

    return token or "nohost"

def _severity(code_raw: str | None) -> int:
    key = _normalize_reply(code_raw)
    return _DYNDNS2_SEVERITY.get(key, 50)

# --- END: Severity handling ---


class DynDNSUpdateView(HomeAssistantView):
    url = UPDATE_PATH
    name = "dyndns_manager:update"
    requires_auth = False

    def __init__(self, hass: HomeAssistant) -> None:
        self.hass = hass

    async def get(self, request):
        params = request.rel_url.query
        username = params.get("username")
        password = params.get("password")
        ipv4 = params.get("ipv4")
        ipv6 = params.get("ipv6")

        # Optional BasicAuth Header
        if (not username or not password) and request.headers.get("Authorization"):
            try:
                auth = BasicAuth.decode(request.headers.get("Authorization").split(" ", 1)[1])
                username = username or auth.login
                password = password or auth.password
            except Exception:
                pass

        # 'myip' akzeptieren und passend zuordnen
        myip = params.get("myip")
        if myip and not ipv4 and not ipv6:
            if ":" in myip:
                ipv6 = myip
            else:
                ipv4 = myip

        # IP-Typen entwirren
        t4, t6 = _classify_ip(ipv4), _classify_ip(ipv6)
        if t4 == "v6" and t6 is None:
            ipv6, ipv4 = ipv4, None
        elif t6 == "v4" and t4 is None:
            ipv4, ipv6 = ipv6, None

        # Alle passenden Einträge sammeln
        matched_entries = []
        for eid, data in self.hass.data.get(DOMAIN, {}).items():
            if not isinstance(data, dict) or eid.startswith("_"):
                continue
            if username == data.get("web_user") and password == data.get("web_pass"):
                matched_entries.append(eid)

        if not matched_entries:
            # kein Gerät mit diesen Zugangsdaten
            return web.Response(text="badauth")

        # Alle passenden Einträge aktualisieren und kritischste (volle) Antwortzeile bestimmen
        worst_score = -1
        worst_reply = None

        for eid in matched_entries:
            entry = self.hass.config_entries.async_get_entry(eid)
            results = await self._update_all_for_entry(entry, ipv4, ipv6)

            for res in results.values():
                # Bevorzuge Rohantwort mit IP etc., fallback auf Codes
                payload = res.get("resp") or res.get("dyndns2") or res.get("status")

                # in Liste nicht-leerer Zeilen normalisieren
                if payload is None:
                    lines = []
                elif isinstance(payload, str):
                    lines = [ln.strip() for ln in payload.splitlines() if ln.strip()]
                elif isinstance(payload, (list, tuple)):
                    lines = []
                    for item in payload:
                        if item is None:
                            continue
                        if isinstance(item, str):
                            lines.extend([ln.strip() for ln in item.splitlines() if ln.strip()])
                        else:
                            s = str(item).strip()
                            if s:
                                lines.append(s)
                else:
                    s = str(payload).strip()
                    lines = [s] if s else []

                # jede Zeile bewerten (erstes Token wird in _normalize_reply berücksichtigt)
                for line in lines:
                    score = _severity(line)
                    if score > worst_score:
                        worst_score = score
                        worst_reply = line

        return web.Response(text=(worst_reply or "911"))

    async def _update_all_for_entry(self, entry: ConfigEntry, ipv4: str | None, ipv6: str | None):
        from .provider import get_provider
        import aiohttp

        data = self.hass.data[DOMAIN][entry.entry_id]
        provider = get_provider(data["provider"])
        results = {}
        async with aiohttp.ClientSession() as session:
            for dom in data["domains"]:
                try:
                    status_text, dyndns2, resp_text, eff_v4, eff_v6 = await provider.update_domain(
                        session=session,
                        credentials=entry.data | entry.options,
                        domain=dom,
                        ipv4=ipv4,
                        ipv6=ipv6,
                    )
                    data["last_results"][dom] = {
                        "status": dyndns2,
                        "dyndns2": dyndns2,
                        "resp": resp_text,
                        "ipv4": eff_v4 or "Unbekannt",
                        "ipv6": eff_v6 or "Unbekannt",
                        "ts": datetime.now(timezone.utc).isoformat(),
                    }
                    results[dom] = data["last_results"][dom]
                except Exception as ex:
                    data["last_results"][dom] = {
                        "status": "error",
                        "dyndns2": "911",
                        "resp": str(ex),
                        "ipv4": ipv4,
                        "ipv6": ipv6,
                        "ts": datetime.now(timezone.utc).isoformat(),
                    }
                    results[dom] = data["last_results"][dom]

        # Entities des EINEN Eintrags updaten
        async_dispatcher_send(self.hass, SIGNAL_RESULTS_UPDATED, entry.entry_id)
        return results