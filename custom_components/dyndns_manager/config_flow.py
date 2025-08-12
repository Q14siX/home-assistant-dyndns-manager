
from __future__ import annotations
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.helpers.selector import (
    SelectSelector, SelectSelectorConfig, SelectSelectorMode,
    TextSelector, TextSelectorConfig, TextSelectorType,
)
from .const import (
    DOMAIN, CONF_PROVIDER, CONF_DOMAINS, CONF_WEB_USER, CONF_WEB_PASS,
    PROVIDER_CLOUDFLARE, PROVIDER_DUCKDNS, PROVIDER_STRATO
)

PROVIDER_OPTIONS = [PROVIDER_CLOUDFLARE, PROVIDER_DUCKDNS, PROVIDER_STRATO]
PROVIDER_OPTIONS.sort()

def _parse_domains(text: str) -> list[str]:
    if not text:
        return []
    parts = [p.strip() for p in text.replace("\n", ",").split(",")]
    return [p for p in parts if p]

class DynDNSConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    def __init__(self):
        self._provider = None
        self._provider_creds = {}
        self._domains: list[str] = []

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            self._provider = user_input[CONF_PROVIDER]
            return await self.async_step_provider()

        schema = vol.Schema({
            vol.Required(CONF_PROVIDER): SelectSelector(
                SelectSelectorConfig(
                    options=PROVIDER_OPTIONS,
                    mode=SelectSelectorMode.DROPDOWN,
                )
            ),
        })
        return self.async_show_form(step_id="user", data_schema=schema)

    async def async_step_provider(self, user_input=None):
        if user_input is not None:
            self._provider_creds = dict(user_input)
            return await self.async_step_domains()

        if self._provider == PROVIDER_DUCKDNS:
            schema = vol.Schema({
                vol.Required("duckdns_token"): TextSelector(TextSelectorConfig(type=TextSelectorType.PASSWORD)),
            })
        elif self._provider == PROVIDER_CLOUDFLARE:
            schema = vol.Schema({
                vol.Required("cf_api_token"): TextSelector(TextSelectorConfig(type=TextSelectorType.PASSWORD)),
            })
        else:  # STRATO
            schema = vol.Schema({
                vol.Required("strato_user"): TextSelector(TextSelectorConfig(type=TextSelectorType.TEXT)),
                vol.Required("strato_pass"): TextSelector(TextSelectorConfig(type=TextSelectorType.PASSWORD)),
            })

        return self.async_show_form(step_id="provider", data_schema=schema)

    async def async_step_domains(self, user_input=None):
        if user_input is not None:
            raw = user_input.get(CONF_DOMAINS, "")
            self._domains = _parse_domains(raw)
            return await self.async_step_webaccess()

        schema = vol.Schema({
            vol.Required(CONF_DOMAINS): TextSelector(TextSelectorConfig(type=TextSelectorType.TEXT)),
        })
        return self.async_show_form(step_id="domains", data_schema=schema)

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
        self._provider_creds = {}
        self._domains: list[str] = []

    async def async_step_init(self, user_input=None):
        return await self.async_step_provider()

    async def async_step_provider(self, user_input=None):
        provider = self.entry.data.get(CONF_PROVIDER)
        if user_input is not None:
            self._provider_creds = dict(user_input)
            return await self.async_step_domains()

        if provider == PROVIDER_DUCKDNS:
            schema = vol.Schema({
                vol.Required("duckdns_token", default=self.entry.data.get("duckdns_token", "")): TextSelector(TextSelectorConfig(type=TextSelectorType.PASSWORD)),
            })
        elif provider == PROVIDER_CLOUDFLARE:
            schema = vol.Schema({
                vol.Required("cf_api_token", default=self.entry.data.get("cf_api_token", "")): TextSelector(TextSelectorConfig(type=TextSelectorType.PASSWORD)),
            })
        else:
            schema = vol.Schema({
                vol.Required("strato_user", default=self.entry.data.get("strato_user", "")): TextSelector(TextSelectorConfig(type=TextSelectorType.TEXT)),
                vol.Required("strato_pass", default=self.entry.data.get("strato_pass", "")): TextSelector(TextSelectorConfig(type=TextSelectorType.PASSWORD)),
            })

        return self.async_show_form(step_id="provider", data_schema=schema)

    async def async_step_domains(self, user_input=None):
        if user_input is not None:
            raw = user_input.get(CONF_DOMAINS, "")
            self._domains = _parse_domains(raw)
            return await self.async_step_webaccess()

        current = (self.entry.options.get(CONF_DOMAINS) if self.entry.options else None) or self.entry.data.get(CONF_DOMAINS, [])
        preset = ", ".join(current) if isinstance(current, list) else (current or "")
        schema = vol.Schema({
            vol.Required(CONF_DOMAINS, default=preset): TextSelector(TextSelectorConfig(type=TextSelectorType.TEXT)),
        })
        return self.async_show_form(step_id="domains", data_schema=schema)

    async def async_step_webaccess(self, user_input=None):
        if user_input is not None:
            options = {
                CONF_DOMAINS: self._domains,
                CONF_WEB_USER: user_input[CONF_WEB_USER],
                CONF_WEB_PASS: user_input[CONF_WEB_PASS],
            }
            return self.async_create_entry(title="", data=options)

        schema = vol.Schema({
            vol.Required(CONF_WEB_USER, default=(self.entry.options.get(CONF_WEB_USER) if self.entry.options else None) or self.entry.data.get(CONF_WEB_USER, "")): TextSelector(TextSelectorConfig(type=TextSelectorType.TEXT)),
            vol.Required(CONF_WEB_PASS, default=(self.entry.options.get(CONF_WEB_PASS) if self.entry.options else None) or self.entry.data.get(CONF_WEB_PASS, "")): TextSelector(TextSelectorConfig(type=TextSelectorType.PASSWORD)),
        })
        return self.async_show_form(step_id="webaccess", data_schema=schema)
