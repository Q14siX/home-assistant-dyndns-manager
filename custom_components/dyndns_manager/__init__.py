
from __future__ import annotations

import logging
from datetime import datetime, timezone
from aiohttp import web, BasicAuth

from homeassistant.core import HomeAssistant, callback
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.components.http import HomeAssistantView
from homeassistant.helpers.dispatcher import async_dispatcher_send

from .const import (
    DOMAIN,
    CONF_PROVIDER, CONF_DOMAINS, CONF_WEB_USER, CONF_WEB_PASS,
    UPDATE_PATH,
    SIGNAL_DOMAINS_UPDATED, SIGNAL_RESULTS_UPDATED,
)

_LOGGER = logging.getLogger(__name__)


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

    # Update listener for live domain changes without full reload
    async def _options_updated(hass_: HomeAssistant, updated_entry: ConfigEntry):
        data = hass.data[DOMAIN][updated_entry.entry_id]
        merged = _merged_entry_data(updated_entry)
        data["domains"] = merged.get(CONF_DOMAINS, [])
        data["web_user"] = merged.get(CONF_WEB_USER)
        data["web_pass"] = merged.get(CONF_WEB_PASS)
        # tell platforms to sync entities
        async_dispatcher_send(hass, SIGNAL_DOMAINS_UPDATED, updated_entry.entry_id, list(data["domains"]))

    entry.async_on_unload(entry.add_update_listener(_options_updated))

    # Register HTTP view for Fritz!Box style updates
    try:
        hass.http.register_view(DynDNSUpdateView(hass, entry))
    except Exception:
        pass

    await hass.config_entries.async_forward_entry_setups(entry, [Platform.SENSOR, Platform.BUTTON])
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    unload_ok = await hass.config_entries.async_unload_platforms(entry, [Platform.SENSOR, Platform.BUTTON])
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id, None)
    return unload_ok


def _classify_ip(ip: str | None):
    if not ip:
        return None
    try:
        addr = ip.strip()
        ipaddress.ip_address(addr)  # type: ignore[name-defined]
        return "v6" if ":" in addr else "v4"
    except Exception:
        return None


class DynDNSUpdateView(HomeAssistantView):
    url = UPDATE_PATH
    name = "dyndns_manager:update"
    requires_auth = False

    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None:
        self.hass = hass
        self.entry = entry

    async def get(self, request):
        params = request.rel_url.query
        username = params.get("username")
        password = params.get("password")
        ipv4 = params.get("ipv4")
        ipv6 = params.get("ipv6")

        # Support HTTP Basic Auth (DynDNS2 standard) if query credentials are absent
        if (not username or not password) and request.headers.get("Authorization"):
            try:
                auth = BasicAuth.decode(request.headers.get("Authorization").split(" ", 1)[1])
                if not username:
                    username = auth.login
                if not password:
                    password = auth.password
            except Exception:
                # Ignore malformed Authorization; fall back to any provided query params
                pass

        # Support 'myip' parameter per DynDNS2; map to ipv4/ipv6 if provided
        myip = params.get("myip")
        if myip and not ipv4 and not ipv6:
            if ":" in myip:
                ipv6 = myip
            else:
                ipv4 = myip

        data = self.hass.data[DOMAIN].get(self.entry.entry_id, {})
        if not data:
            return web.Response(text="911")

        # Web access guard: only enforce if set
        if (data.get("web_user") or data.get("web_pass")):
            if username != data.get("web_user") or password != data.get("web_pass"):
                return web.Response(text="badauth")

        # Auto-correct swapped IPs if needed
        t4, t6 = _classify_ip(ipv4), _classify_ip(ipv6)
        if t4 == "v6" and t6 is None:
            ipv6, ipv4 = ipv4, None
        elif t6 == "v4" and t4 is None:
            ipv4, ipv6 = ipv6, None

        results = await self._update_all(ipv4=ipv4, ipv6=ipv6)

        

        if results:
            # Wähle die kritischste DynDNS2-Antwort (ohne Auth-Fehler, die oben behandelt sind)
            priority = [
                "911", "dnserr", "abuse", "badauth", "badagent", "notfqdn",
                "nohost", "numhost", "!yours", "nochg", "good"
            ]
            def rank(res):
                code = (res.get("dyndns2","") or "").split()[0].lower()
                try:
                    return priority.index(code)
                except ValueError:
                    return 2  # unbekannt ~ 'abuse'
            worst = min(results.values(), key=rank)
            # Für die URL geben wir die Original-Servermeldung zurück (inkl. IP, falls enthalten)
            server_text = (worst.get("resp") or "").strip()
            reply = server_text if server_text else (worst.get("dyndns2") or "911")
            return web.Response(text=reply)
        return web.Response(text="911")


    async def _update_all(self, ipv4: str | None, ipv6: str | None):
        from .provider import get_provider
        import aiohttp

        data = self.hass.data[DOMAIN][self.entry.entry_id]
        provider_name = data["provider"]
        domains = data["domains"]
        provider = get_provider(provider_name)

        results = {}
        async with aiohttp.ClientSession() as session:
            for dom in domains:
                try:
                    status_text, dyndns2, resp_text, eff_v4, eff_v6 = await provider.update_domain(
                        session=session,
                        credentials=self.entry.data | self.entry.options,
                        domain=dom,
                        ipv4=ipv4,
                        ipv6=ipv6,
                    )
                    data["last_results"][dom] = {
                        "status": dyndns2,
                        "dyndns2": dyndns2,
                        "resp": resp_text,
                        "ipv4": eff_v4 if eff_v4 is not None else "Unbekannt",
                        "ipv6": eff_v6 if eff_v6 is not None else "Unbekannt",
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

        # Notify entities to refresh state
        async_dispatcher_send(self.hass, SIGNAL_RESULTS_UPDATED, self.entry.entry_id)
        return results