from __future__ import annotations
from homeassistant.components.button import ButtonEntity
from homeassistant.helpers.entity import DeviceInfo
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    data = hass.data[DOMAIN][entry.entry_id]
    provider = data.get("provider")
    device_info = DeviceInfo(
        identifiers={(DOMAIN, entry.entry_id)},
        name=f"DynDNS Manager ({provider})",
        manufacturer="DynDNS Manager",
        model=provider,
    )
    async_add_entities([UpdateAllDomainsButton(hass, entry, device_info)])

class UpdateAllDomainsButton(ButtonEntity):
    _attr_icon = "mdi:update"
    _attr_name = "Update Domains"

    def __init__(self, hass, entry, device_info):
        self.hass = hass
        self.entry = entry
        self._attr_unique_id = f"{entry.entry_id}_update_all"
        self._attr_device_info = device_info

    async def async_press(self) -> None:
        # nur diese Integration updaten
        from . import DynDNSUpdateView
        view = DynDNSUpdateView(self.hass)
        await view._update_all_for_entry(self.entry, ipv4=None, ipv6=None)
