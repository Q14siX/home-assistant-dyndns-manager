from __future__ import annotations

from typing import Any, Dict

from homeassistant.components.sensor import SensorEntity, SensorDeviceClass
from homeassistant.const import STATE_UNKNOWN, STATE_UNAVAILABLE
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect
from homeassistant.helpers import entity_registry as er
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import (
    DOMAIN,
    ATTR_IPV4,
    ATTR_IPV6,
    ATTR_LAST_RESPONSE,
    ATTR_LAST_UPDATE,
    SIGNAL_DOMAINS_UPDATED,
    SIGNAL_RESULTS_UPDATED,
    DynDNSStatus,
    DYNDNS_STATE_OPTIONS,
)

# Platform state: map entry_id -> domain -> entity
PLAT_STATE: dict[str, dict[str, "DomainStatusSensor"]] = {}


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None:
    data = hass.data[DOMAIN][entry.entry_id]
    provider = data.get("provider")
    device_info = DeviceInfo(
        identifiers={(DOMAIN, entry.entry_id)},
        name=f"DynDNS Manager ({provider})",
        manufacturer="DynDNS Manager",
        model=provider,
    )

    domain_list = list(data.get("domains", []))
    entities = [DomainStatusSensor(hass, entry, device_info, d) for d in domain_list]
    if entities:
        async_add_entities(entities)

    # keep state map
    PLAT_STATE.setdefault(entry.entry_id, {})
    for ent in entities:
        PLAT_STATE[entry.entry_id][ent.domain_name] = ent

    # react to domain list changes (options flow)
    async def _on_domains_update(entry_id: str, domains: list[str]) -> None:
        if entry_id != entry.entry_id:
            return
        domains = list(domains or [])
        existing = PLAT_STATE.get(entry.entry_id, {})
        to_add = [d for d in domains if d not in existing]
        to_remove = [d for d in list(existing.keys()) if d not in domains]

        new_entities: list[DomainStatusSensor] = []
        for d in to_add:
            ent = DomainStatusSensor(hass, entry, device_info, d)
            new_entities.append(ent)
            existing[d] = ent

        if new_entities:
            async_add_entities(new_entities)

        # remove entities that are no longer configured
        for d in to_remove:
            ent = existing.pop(d, None)
            if ent:
                ent.async_remove()
                # ensure it's gone from the entity registry as well
                try:
                    registry = er.async_get(hass)
                    unique_id = f"{entry.entry_id}_{d}"
                    entity_id = registry.async_get_entity_id("sensor", DOMAIN, unique_id)
                    if entity_id:
                        registry.async_remove(entity_id)
                except Exception:
                    pass

    entry.async_on_unload(async_dispatcher_connect(hass, SIGNAL_DOMAINS_UPDATED, _on_domains_update))

    # react to results updates (service/refresh)
    async def _on_results_update(entry_id: str) -> None:
        if entry_id != entry.entry_id:
            return
        for ent in PLAT_STATE.get(entry.entry_id, {}).values():
            ent.async_write_ha_state()

    entry.async_on_unload(async_dispatcher_connect(hass, SIGNAL_RESULTS_UPDATED, _on_results_update))


class DomainStatusSensor(SensorEntity):
    _attr_has_entity_name = True
    _attr_icon = "mdi:web"
    _attr_translation_key = "domain_status"
    _attr_device_class = SensorDeviceClass.ENUM
    _attr_options = DYNDNS_STATE_OPTIONS

    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, device_info: DeviceInfo, domain: str) -> None:
        self.hass = hass
        self.entry = entry
        self._domain = domain
        self._attr_unique_id = f"{entry.entry_id}_{domain}"
        self._attr_name = domain
        self._attr_device_info = device_info

    @property
    def domain_name(self) -> str:
        return self._domain

    @property
    def native_value(self) -> str:
        # Determine current status from hass.data written by __init__.py updater
        st = self.hass.data[DOMAIN][self.entry.entry_id]["last_results"].get(self._domain)
        if not st:
            return STATE_UNKNOWN
        # dyndns2 style: code and maybe arguments, e.g. "good 1.2.3.4"
        raw_code = (st.get("dyndns2") or "").split()[0].strip().lower()
        if not raw_code:
            return STATE_UNKNOWN
        return self._normalize_code(raw_code)

    def _normalize_code(self, raw: str) -> str:
        # normalize special / alias forms
        if raw == "nofqdn":
            raw = DynDNSStatus.NOTFQDN.value
        if raw in ("servererror", "providererror"):
            raw = DynDNSStatus.S_911.value

        # Accept value if in our enum option list
        if raw in self.options:
            return raw

        # Fallbacks
        if raw in {"unknown", "unavailable"}:
            return raw
        return DynDNSStatus.ERROR.value

    @property
    def available(self) -> bool:
        # We keep sensors available; state conveys issues
        return True

    @property
    def extra_state_attributes(self) -> Dict[str, Any]:
        st = self.hass.data[DOMAIN][self.entry.entry_id]["last_results"].get(self._domain, {})
        return {
            ATTR_LAST_UPDATE: st.get("ts") or STATE_UNKNOWN,
            ATTR_IPV4: st.get("ipv4") or STATE_UNKNOWN,
            ATTR_IPV6: st.get("ipv6") or STATE_UNKNOWN,
            ATTR_LAST_RESPONSE: st.get("resp") or STATE_UNKNOWN,
        }
