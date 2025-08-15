from __future__ import annotations

import asyncio
import logging
from urllib.parse import urlparse

import aiohttp
import voluptuous as vol
from homeassistant.core import HomeAssistant, ServiceCall
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.network import get_url

from .const import DOMAIN, CONF_WEB_USER, CONF_WEB_PASS

_LOGGER = logging.getLogger(__name__)

SERVICE_CALL_UPDATE = "call_update"

SCHEMA_CALL_UPDATE = vol.Schema(
    {
        vol.Optional("ha_host"): cv.string,        # optional, Default = aus HA-URL
        vol.Optional("ha_port"): cv.positive_int,  # optional, Default = aus HA-URL
        vol.Optional("web_username"): cv.string,   # optional, Default = aus Entry (wenn nur 1)
        vol.Optional("web_password"): cv.string,   # optional, Default = aus Entry (wenn nur 1)
        # Checkbox + Textbox Logik:
        vol.Optional("use_ipv4", default=False): cv.boolean,
        vol.Optional("ipv4"): cv.string,           # wenn leer/fehlend und use_ipv4=True -> extern holen
        vol.Optional("use_ipv6", default=False): cv.boolean,
        vol.Optional("ipv6"): cv.string,           # wenn leer/fehlend und use_ipv6=True -> extern holen
        vol.Optional("timeout", default=10): cv.positive_int,
    }
)

_registered = False

# --- Hilfsfunktionen für externe IP-Ermittlung ---
_IP_TIMEOUT = aiohttp.ClientTimeout(total=3)

async def _fetch_text(session: aiohttp.ClientSession, url: str) -> str | None:
    try:
        async with session.get(url, timeout=_IP_TIMEOUT) as resp:
            if resp.status == 200:
                text = (await resp.text()).strip()
                if text and len(text) <= 64:
                    return text
    except Exception as exc:
        _LOGGER.debug("External IP fetch failed for %s: %s", url, exc)
    return None

async def _get_external_ipv4() -> str | None:
    """Hole öffentliche IPv4 über v4-only Endpunkte."""
    urls = [
        "https://api4.ipify.org",
        "https://ipv4.icanhazip.com",
        "https://v4.ident.me",
    ]
    async with aiohttp.ClientSession() as session:
        for url in urls:
            ip = await _fetch_text(session, url)
            if ip:
                return ip
    return None

async def _get_external_ipv6() -> str | None:
    """Hole öffentliche IPv6 über v6-only Endpunkte."""
    urls = [
        "https://api6.ipify.org",
        "https://ipv6.icanhazip.com",
        "https://v6.ident.me",
    ]
    async with aiohttp.ClientSession() as session:
        for url in urls:
            ip = await _fetch_text(session, url)
            if ip:
                return ip
    return None
# --- Ende Hilfsfunktionen ---


async def async_setup_services(hass: HomeAssistant) -> None:
    """Register HA services (idempotent)."""
    global _registered
    if _registered:
        return

    async def _handle_call_update(call: ServiceCall) -> None:
        # 1) Host/Port aus aktueller HA-URL ableiten
        base = get_url(hass)
        parsed = urlparse(base)
        default_host = parsed.hostname or "localhost"
        default_port = parsed.port or (443 if parsed.scheme == "https" else 8123)

        ha_host = call.data.get("ha_host", default_host)
        ha_port = call.data.get("ha_port", default_port)

        # 2) IPv4/IPv6 Behandlung gemäß Checkbox + Textbox
        ipv4_param: str | None = None
        ipv6_param: str | None = None

        # IPv4
        if call.data.get("use_ipv4", False):
            raw_v4 = call.data.get("ipv4")
            if raw_v4:  # Textbox gefüllt
                ipv4_param = raw_v4
            else:       # Textbox leer -> extern holen
                v4 = await _get_external_ipv4()
                if v4:
                    ipv4_param = v4
                else:
                    _LOGGER.warning("use_ipv4 checked, but could not determine external IPv4.")

        # IPv6
        if call.data.get("use_ipv6", False):
            raw_v6 = call.data.get("ipv6")
            if raw_v6:  # Textbox gefüllt
                ipv6_param = raw_v6
            else:       # Textbox leer -> extern holen
                v6 = await _get_external_ipv6()
                if v6:
                    ipv6_param = v6
                else:
                    _LOGGER.info("use_ipv6 checked, but could not determine external IPv6.")

        # 3) Credentials: wenn genau EIN ConfigEntry existiert, daraus übernehmen
        entries = [e for e in hass.config_entries.async_entries(DOMAIN)]
        web_username = call.data.get("web_username")
        web_password = call.data.get("web_password")

        if (web_username is None or web_password is None) and len(entries) == 1:
            merged = {**(entries[0].data or {}), **(entries[0].options or {})}
            web_username = web_username or merged.get(CONF_WEB_USER, "")
            web_password = web_password or merged.get(CONF_WEB_PASS, "")

        web_username = web_username or ""
        web_password = web_password or ""

        timeout = call.data["timeout"]

        # 4) Ziel-URL bauen: nur Parameter anhängen, wenn use_* True und wir einen Wert haben
        url = f"http://{ha_host}:{ha_port}/dyndns-manager/?username={web_username}&password={web_password}"
        if call.data.get("use_ipv4", False) and ipv4_param:
            url += f"&ipv4={ipv4_param}"
        if call.data.get("use_ipv6", False) and ipv6_param:
            url += f"&ipv6={ipv6_param}"

        _LOGGER.debug("Calling DynDNS update URL: %s", url)

        # 5) GET ausführen
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, timeout=timeout) as resp:
                    body = await resp.text()
                    _LOGGER.info("DynDNS call -> HTTP %s", resp.status)
                    hass.bus.async_fire(
                        f"{DOMAIN}_call_update_done",
                        {"status": resp.status, "body": body, "url": url},
                    )
        except asyncio.TimeoutError:
            _LOGGER.error("DynDNS call timed out after %ss: %s", timeout, url)
            hass.bus.async_fire(
                f"{DOMAIN}_call_update_error", {"error": "timeout", "url": url}
            )
        except Exception as exc:
            _LOGGER.exception("DynDNS call failed: %s", exc)
            hass.bus.async_fire(
                f"{DOMAIN}_call_update_error", {"error": str(exc), "url": url}
            )

    hass.services.async_register(
        DOMAIN, SERVICE_CALL_UPDATE, _handle_call_update, schema=SCHEMA_CALL_UPDATE
    )
    _registered = True
    _LOGGER.debug("Service '%s.%s' registered", DOMAIN, SERVICE_CALL_UPDATE)


async def async_unload_services(hass: HomeAssistant) -> None:
    """Unregister HA services (idempotent)."""
    global _registered
    if _registered:
        hass.services.async_remove(DOMAIN, SERVICE_CALL_UPDATE)
        _registered = False
        _LOGGER.debug("All services for '%s' removed", DOMAIN)
