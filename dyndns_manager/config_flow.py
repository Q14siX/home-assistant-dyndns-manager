from __future__ import annotations
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.helpers.selector import (
    SelectSelector, SelectSelectorConfig, SelectSelectorMode,
    TextSelector, TextSelectorConfig, TextSelectorType,
)
from .const import (
    DOMAIN, CONF_PROVIDER, CONF_DOMAIN, CONF_DOMAINS, CONF_WEB_USER, CONF_WEB_PASS,
    PROVIDER_CLOUDFLARE, PROVIDER_DUCKDNS, PROVIDER_STRATO, PROVIDER_ALLINKL, PROVIDER_NOIP
)

PROVIDER_OPTIONS = [PROVIDER_CLOUDFLARE, PROVIDER_DUCKDNS, PROVIDER_STRATO, PROVIDER_ALLINKL, PROVIDER_NOIP]
PROVIDER_OPTIONS.sort(key=str.lower)


def _parse_domains(raw: str) -> list[str]:
    parts = [p.strip() for p in (raw or "").replace(";", ",").split(",")]
    return [p for p in parts if p]


class DynDNSConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    def __init__(self):
        self._provider: str | None = None
        self._provider_creds: dict = {}
        self._domains: list[str] = []

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            self._provider = user_input[CONF_PROVIDER]
            return await self.async_step_provider()

        schema = vol.Schema({
            vol.Required(CONF_PROVIDER): SelectSelector(
                SelectSelectorConfig(options=PROVIDER_OPTIONS, mode=SelectSelectorMode.DROPDOWN)
            )
        })
        return self.async_show_form(step_id="user", data_schema=schema)

    async def async_step_provider(self, user_input=None):
        if user_input is not None:
            self._provider_creds = dict(user_input)
            return await self.async_step_domains()

        # provider-specific credentials
        if self._provider == PROVIDER_DUCKDNS:
            schema = vol.Schema({
                vol.Required("duckdns_token"): TextSelector(TextSelectorConfig(type=TextSelectorType.PASSWORD)),
            })
        elif self._provider == PROVIDER_CLOUDFLARE:
            schema = vol.Schema({
                vol.Required("cf_api_token"): TextSelector(TextSelectorConfig(type=TextSelectorType.PASSWORD)),
            })
        elif self._provider == PROVIDER_ALLINKL:
            schema = vol.Schema({
                vol.Required("allinkl_user"): TextSelector(TextSelectorConfig(type=TextSelectorType.TEXT)),
                vol.Required("allinkl_pass"): TextSelector(TextSelectorConfig(type=TextSelectorType.PASSWORD)),
            })
        elif self._provider == PROVIDER_NOIP:
            schema = vol.Schema({
                vol.Required("noip_user"): TextSelector(TextSelectorConfig(type=TextSelectorType.TEXT)),
                vol.Required("noip_pass"): TextSelector(TextSelectorConfig(type=TextSelectorType.PASSWORD)),
            })
        else:  # STRATO
            schema = vol.Schema({
                vol.Required("strato_user"): TextSelector(TextSelectorConfig(type=TextSelectorType.TEXT)),
                vol.Required("strato_pass"): TextSelector(TextSelectorConfig(type=TextSelectorType.PASSWORD)),
            })

        return self.async_show_form(step_id="provider", data_schema=schema)

    async def async_step_domains(self, user_input=None):
        provider = (getattr(self, "_provider", None) or getattr(self, "provider", None) or "").lower()
        # Single-Mode, wenn Provider All-Inkl ODER per Delegation erzwungen
        is_all_inkl = getattr(self, "_force_single", False) or provider in {"all-inkl.com", "all-inkl"}
        
        field_key = CONF_DOMAIN if is_all_inkl else CONF_DOMAINS
        step_id = "domains_single" if is_all_inkl else "domains"
        
        if user_input is not None:
            # Flag wieder zurücksetzen, damit Folge-Schritte nicht beeinflusst werden
            if hasattr(self, "_force_single"):
                delattr(self, "_force_single")
                
            if is_all_inkl:
                value = user_input.get(CONF_DOMAIN, "")
                self._domains = [value] if isinstance(value, str) and value else []
            else:
                self._domains = user_input.get(CONF_DOMAINS, [])
            return await self.async_step_webaccess()
        
        options = sorted(self._domains or [], key=str.lower)
        multiple = not is_all_inkl
        default = (options[0] if options else "") if not multiple else options
        
        schema = vol.Schema({
            vol.Required(field_key, default=default): SelectSelector(
                SelectSelectorConfig(
                    options=options,
                    multiple=multiple,
                    custom_value=True,
                    mode=SelectSelectorMode.DROPDOWN,
                ),
            ),
        })
        return self.async_show_form(step_id=step_id, data_schema=schema)
    
    async def async_step_domains_single(self, user_input=None):
        # „domains_single“ wird von HA aufgerufen, wenn das Formular mit step_id=domains_single abgesendet wird.
        # Wir erzwingen einmalig den Single-Mode und delegieren an die bestehende Logik.
        self._force_single = True
        return await self.async_step_domains(user_input)
    

    async def async_step_webaccess(self, user_input=None):
        if user_input is not None:
            data = {
                CONF_PROVIDER: self._provider,
                CONF_DOMAINS: self._domains,
                CONF_WEB_USER: user_input[CONF_WEB_USER],
                CONF_WEB_PASS: user_input[CONF_WEB_PASS],
            }
            title = f"DynDNS: {self._provider}"
            return self.async_create_entry(title=title, data={**data, **self._provider_creds})

        schema = vol.Schema({
            vol.Required(CONF_WEB_USER): TextSelector(TextSelectorConfig(type=TextSelectorType.TEXT)),
            vol.Required(CONF_WEB_PASS): TextSelector(TextSelectorConfig(type=TextSelectorType.PASSWORD)),
        })
        return self.async_show_form(step_id="webaccess", data_schema=schema)

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return DynDNSOptionsFlow(config_entry)


class DynDNSOptionsFlow(config_entries.OptionsFlow):
    def __init__(self, entry):
        self.entry = entry
        self._provider_creds: dict = {}
        self._domains: list[str] = []

    async def async_step_init(self, user_input=None):
        # Jump directly to provider creds (with defaults), then domains/webaccess
        return await self.async_step_provider()

    def _merged(self) -> dict:
        # entry.options overrides entry.data
        merged = dict(self.entry.data)
        merged.update(self.entry.options or {})
        return merged

    async def async_step_provider(self, user_input=None):
        merged = self._merged()
        provider = self.entry.data.get(CONF_PROVIDER)

        if user_input is not None:
            self._provider_creds = dict(user_input)
            return await self.async_step_domains()

        # provider-specific defaults
        if provider == PROVIDER_DUCKDNS:
            schema = vol.Schema({
                vol.Required("duckdns_token", default=merged.get("duckdns_token", "")): TextSelector(TextSelectorConfig(type=TextSelectorType.PASSWORD)),
            })
        elif provider == PROVIDER_CLOUDFLARE:
            schema = vol.Schema({
                vol.Required("cf_api_token", default=merged.get("cf_api_token", "")): TextSelector(TextSelectorConfig(type=TextSelectorType.PASSWORD)),
            })
        elif provider == PROVIDER_ALLINKL:
            schema = vol.Schema({
                vol.Required("allinkl_user", default=merged.get("allinkl_user", "")): TextSelector(TextSelectorConfig(type=TextSelectorType.TEXT)),
                vol.Required("allinkl_pass", default=merged.get("allinkl_pass", "")): TextSelector(TextSelectorConfig(type=TextSelectorType.PASSWORD)),
            })
        elif provider == PROVIDER_NOIP:
            schema = vol.Schema({
                vol.Required("noip_user", default=merged.get("noip_user", "")): TextSelector(TextSelectorConfig(type=TextSelectorType.TEXT)),
                vol.Required("noip_pass", default=merged.get("noip_pass", "")): TextSelector(TextSelectorConfig(type=TextSelectorType.PASSWORD)),
            })
        else:  # STRATO
            schema = vol.Schema({
                vol.Required("strato_user", default=merged.get("strato_user", "")): TextSelector(TextSelectorConfig(type=TextSelectorType.TEXT)),
                vol.Required("strato_pass", default=merged.get("strato_pass", "")): TextSelector(TextSelectorConfig(type=TextSelectorType.PASSWORD)),
            })

        return self.async_show_form(step_id="provider", data_schema=schema)

    async def async_step_domains(self, user_input=None):
        merged = self._merged()
        provider = (merged.get(CONF_PROVIDER, "") or "").lower()
        is_all_inkl = getattr(self, "_force_single", False) or provider in {"all-inkl.com", "all-inkl"}
        
        field_key = CONF_DOMAIN if is_all_inkl else CONF_DOMAINS
        step_id = "domains_single" if is_all_inkl else "domains"
        
        if user_input is not None:
            if hasattr(self, "_force_single"):
                delattr(self, "_force_single")
                
            if is_all_inkl:
                value = user_input.get(CONF_DOMAIN, "")
                self._domains = [value] if isinstance(value, str) and value else []
            else:
                self._domains = user_input.get(CONF_DOMAINS, [])
            return await self.async_step_webaccess()
        
        existing = merged.get(CONF_DOMAINS, [])
        options = sorted(existing, key=str.lower)
        multiple = not is_all_inkl
        default = (existing[0] if existing else "") if not multiple else existing
        
        schema = vol.Schema({
            vol.Required(field_key, default=default): SelectSelector(
                SelectSelectorConfig(
                    options=options,
                    multiple=multiple,
                    custom_value=True,
                    mode=SelectSelectorMode.DROPDOWN,
                ),
            ),
        })
        return self.async_show_form(step_id=step_id, data_schema=schema)
    
    async def async_step_domains_single(self, user_input=None):
        self._force_single = True
        return await self.async_step_domains(user_input)
        
    async def async_step_webaccess(self, user_input=None):
        merged = self._merged()
        if user_input is not None:
            options = {
                CONF_DOMAINS: self._domains,
                CONF_WEB_USER: user_input[CONF_WEB_USER],
                CONF_WEB_PASS: user_input[CONF_WEB_PASS],
            }
            # Persist provider credentials alongside options
            return self.async_create_entry(title="", data={**options, **self._provider_creds})

        schema = vol.Schema({
            vol.Required(CONF_WEB_USER, default=merged.get(CONF_WEB_USER, "")): TextSelector(TextSelectorConfig(type=TextSelectorType.TEXT)),
            vol.Required(CONF_WEB_PASS, default=merged.get(CONF_WEB_PASS, "")): TextSelector(TextSelectorConfig(type=TextSelectorType.PASSWORD)),
        })
        return self.async_show_form(step_id="webaccess", data_schema=schema)