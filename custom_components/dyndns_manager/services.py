from __future__ import annotations

import asyncio
import logging
import socket
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
        vol.Optional("myip"): cv.string,           # optional, Default = IPv4 von ha_host
        vol.Optional("timeout", default=10): cv.positive_int,
    }
)

_registered = False


async def async_setup_services(hass: HomeAssistant) -> None:
    """Register HA services (idempotent)."""
    global _registered
    if _registered:
        return

    async def _handle_call_update(call: ServiceCall) -> None:
        # 1) Host/Port aus aktueller HA-URL ableiten
        base = get_url(hass)  # bevorzugt internal_url, sonst external_url
        parsed = urlparse(base)
        default_host = parsed.hostname or "localhost"
        default_port = parsed.port or (443 if parsed.scheme == "https" else 8123)

        ha_host = call.data.get("ha_host", default_host)
        ha_port = call.data.get("ha_port", default_port)

        # 2) IPv4 automatisch aus ha_host auflösen, falls nicht übergeben
        if "myip" in call.data and call.data["myip"]:
            myip = call.data["myip"]
        else:
            try:
                myip = socket.gethostbyname(ha_host)
            except Exception:
                _LOGGER.warning(
                    "Could not resolve IPv4 for host '%s'; falling back to 127.0.0.1",
                    ha_host,
                )
                myip = "127.0.0.1"

        # 3) Credentials: wenn genau EIN ConfigEntry existiert, daraus übernehmen
        entries = [e for e in hass.config_entries.async_entries(DOMAIN)]
        web_username = call.data.get("web_username")
        web_password = call.data.get("web_password")

        if (web_username is None or web_password is None) and len(entries) == 1:
            merged = {**(entries[0].data or {}), **(entries[0].options or {})}
            web_username = web_username or merged.get(CONF_WEB_USER, "")
            web_password = web_password or merged.get(CONF_WEB_PASS, "")

        # Falls immer noch leer, auf leere Strings setzen (Server antwortet dann 401/badauth)
        web_username = web_username or ""
        web_password = web_password or ""

        timeout = call.data["timeout"]

        # 4) Ziel-URL bauen (dein Endpunkt)
        url = (
            f"http://{ha_host}:{ha_port}/dyndns-manager/"
            f"?username={web_username}&password={web_password}&myip={myip}"
        )

        _LOGGER.debug("Calling DynDNS update URL: %s", url)

        # 5) GET ausführen
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, timeout=timeout) as resp:
                    body = await resp.text()
                    _LOGGER.info("DynDNS call -> HTTP %s", resp.status)
                    # Optional: Event für andere Teile der Integration/Automations
                    hass.bus.async_fire(
                        f"{DOMAIN}_call_update_done",
                        {"status": resp.status, "body": body, "url": url},
                    )
        except asyncio.TimeoutError:
            _LOGGER.error("DynDNS call timed out after %ss: %s", timeout, url)
            hass.bus.async_fire(
                f"{DOMAIN}_call_update_error", {"error": "timeout", "url": url}
            )
        except Exception as exc:  # pragma: no cover
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
