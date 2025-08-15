
from __future__ import annotations

import asyncio
import logging
from urllib.parse import urlparse, urlencode
from functools import partial

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
        vol.Optional("ha_host"): cv.string,
        vol.Optional("ha_port"): cv.positive_int,
        vol.Optional("web_username"): cv.string,
        vol.Optional("web_password"): cv.string,
        vol.Optional("use_ipv4", default=False): cv.boolean,
        vol.Optional("use_ipv6", default=False): cv.boolean,
        vol.Optional("ipv4"): cv.string,
        vol.Optional("ipv6"): cv.string,
        vol.Optional("timeout", default=10): cv.positive_int,
    }
)

_registered = False

# --- External IP helpers ---
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
    async with aiohttp.ClientSession() as s:
        for u in (
            "https://api.ipify.org",
            "https://ipv4.icanhazip.com/",
            "https://v4.ident.me/",
        ):
            txt = await _fetch_text(s, u)
            if txt:
                return txt
    return None

async def _get_external_ipv6() -> str | None:
    async with aiohttp.ClientSession() as s:
        for u in (
            "https://api6.ipify.org",
            "https://ipv6.icanhazip.com/",
            "https://v6.ident.me/",
        ):
            txt = await _fetch_text(s, u)
            if txt:
                return txt
    return None

def _current_host_port(hass: HomeAssistant) -> tuple[str, int | None]:
    # get_url may return http(s)://host:port
    base = get_url(hass)
    parsed = urlparse(base)
    host = parsed.hostname or "homeassistant.local"
    port = parsed.port
    if port is None:
        # heuristics: default HA port 8123 for http; 443 for https if not specified
        port = 8123 if parsed.scheme == "http" else 443
    return host, port

def _collect_single_entry_credentials(hass: HomeAssistant) -> tuple[str | None, str | None]:
    """If exactly one config entry exists, return its web creds; otherwise (or if missing) return (None, None)."""
    data = hass.data.get(DOMAIN, {})
    # Exclude internal flags like "_services_registered"
    entry_dicts = [v for k, v in data.items() if isinstance(v, dict) and k != "_services_registered"]
    if len(entry_dicts) == 1:
        d = entry_dicts[0]
        return d.get("web_user"), d.get("web_pass")
    return None, None

async def _handle_call_update(hass: HomeAssistant, call: ServiceCall) -> None:
    # 1) Host/Port
    ha_host = call.data.get("ha_host")
    ha_port = call.data.get("ha_port")
    if not ha_host or not ha_port:
        cur_host, cur_port = _current_host_port(hass)
        if not ha_host:
            ha_host = cur_host
        if not ha_port:
            ha_port = cur_port

    # 2) IP logic (toggles)
    use_ipv4 = bool(call.data.get("use_ipv4", False))
    use_ipv6 = bool(call.data.get("use_ipv6", False))

    if use_ipv4:
        ipv4 = call.data.get("ipv4")
        if not ipv4:
            ipv4 = await _get_external_ipv4() or ""
    else:
        ipv4 = ""

    if use_ipv6:
        ipv6 = call.data.get("ipv6")
        if not ipv6:
            ipv6 = await _get_external_ipv6() or ""
    else:
        ipv6 = ""

    # 3) Credentials
    web_user = call.data.get("web_username")
    web_pass = call.data.get("web_password")
    if (not web_user or not web_pass):
        u2, p2 = _collect_single_entry_credentials(hass)
        if web_user is None and u2:
            web_user = u2
        if web_pass is None and p2:
            web_pass = p2

    if not web_user or not web_pass:
        _LOGGER.warning("No credentials provided and could not derive from a single entry -> will likely result in badauth.")
    # 4) Build URL
    params = {
        "username": web_user or "",
        "password": web_pass or "",
    }
    if ipv4:
        params["ipv4"] = ipv4
    if ipv6:
        params["ipv6"] = ipv6

    query = urlencode(params)
    url = f"http://{ha_host}:{ha_port}/dyndns-manager/?{query}"
    timeout = aiohttp.ClientTimeout(total=call.data.get("timeout", 10))

    # 5) Call and fire events
    try:
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(url) as resp:
                text = (await resp.text()).strip()
                status = resp.status
                success = status == 200
                if success:
                    hass.bus.fire(f"{DOMAIN}_call_update_done", {"status": status, "body": text, "url": url})
                else:
                    hass.bus.fire(f"{DOMAIN}_call_update_error", {"status": status, "body": text, "url": url})
    except asyncio.TimeoutError:
        hass.bus.fire(f"{DOMAIN}_call_update_error", {"error": "timeout", "url": url})
    except Exception as exc:
        hass.bus.fire(f"{DOMAIN}_call_update_error", {"error": str(exc), "url": url})

async def async_setup_services(hass: HomeAssistant) -> None:
    """Register HA services (idempotent)."""
    global _registered
    if _registered:
        return
    hass.services.async_register(
        DOMAIN, SERVICE_CALL_UPDATE, partial(_handle_call_update, hass), schema=SCHEMA_CALL_UPDATE
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
