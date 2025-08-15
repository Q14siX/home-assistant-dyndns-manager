
from __future__ import annotations

from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.const import STATE_UNAVAILABLE
from homeassistant.helpers.dispatcher import async_dispatcher_connect
from homeassistant.helpers import entity_registry as er
from homeassistant.const import STATE_UNKNOWN

from .const import (
    DOMAIN, ATTR_IPV4, ATTR_IPV6, ATTR_LAST_RESPONSE, ATTR_LAST_UPDATE,
    SIGNAL_DOMAINS_UPDATED, SIGNAL_RESULTS_UPDATED
)

# Platform state: map entry_id -> domain -> entity
PLAT_STATE: dict[str, dict[str, DomainStatusSensor]] = {}  # type: ignore[name-defined]

async def async_setup_entry(hass, entry, async_add_entities):
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
    PLAT_STATE[entry.entry_id] = {e._domain: e for e in entities}
    async_add_entities(entities)

    async def _on_domains_update(entry_id: str, new_domains: list[str]):
        if entry_id != entry.entry_id:
            return
        store = PLAT_STATE.setdefault(entry.entry_id, {})
        existing_domains = set(store.keys())
        new_domains_set = set(new_domains)

        to_add = sorted(list(new_domains_set - existing_domains))
        to_remove = sorted(list(existing_domains - new_domains_set))

        # Add new ones
        new_entities = []
        for d in to_add:
            ent = DomainStatusSensor(hass, entry, device_info, d)
            store[d] = ent
            new_entities.append(ent)
        if new_entities:
            async_add_entities(new_entities)

        # Remove old ones
        for d in to_remove:
            ent = store.pop(d, None)
            if ent:
                # remove live entity
                hass.async_create_task(ent.async_remove())
            # also drop last_results to avoid lingering attributes
            hass.data[DOMAIN][entry.entry_id]["last_results"].pop(d, None)
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
    async def _on_results_update(entry_id: str):
        if entry_id != entry.entry_id:
            return
        for ent in PLAT_STATE.get(entry.entry_id, {}).values():
            ent.async_write_ha_state()

    entry.async_on_unload(async_dispatcher_connect(hass, SIGNAL_RESULTS_UPDATED, _on_results_update))
    
    
class DomainStatusSensor(SensorEntity):
    _attr_icon = "mdi:web"
    _attr_has_entity_name = True
    _attr_translation_key = "domain_status"

    def __init__(self, hass, entry, device_info, domain: str):
        self.hass = hass
        self.entry = entry
        self._domain = domain
        self._attr_unique_id = f"{entry.entry_id}_{domain}"
        self._attr_name = domain
        self._attr_device_info = device_info

    @property
    def native_value(self):
        st = self.hass.data[DOMAIN][self.entry.entry_id]["last_results"].get(self._domain)
        if not st:
            return STATE_UNKNOWN
        code = (st.get("dyndns2") or "").split()[0].strip().lower()
        if not code:
            return STATE_UNKNOWN
        return code

    @property
    def extra_state_attributes(self):
        st = self.hass.data[DOMAIN][self.entry.entry_id]["last_results"].get(self._domain, {})
        return {
            ATTR_LAST_UPDATE: st.get("ts") or STATE_UNKNOWN,
            ATTR_IPV4: st.get("ipv4") or STATE_UNKNOWN,
            ATTR_IPV6: st.get("ipv6") or STATE_UNKNOWN,
            ATTR_LAST_RESPONSE: st.get("resp") or STATE_UNKNOWN,
        }