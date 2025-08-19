from __future__ import annotations

from enum import StrEnum

DOMAIN = "dyndns_manager"

CONF_PROVIDER = "provider"
CONF_DOMAIN = "domain"
CONF_DOMAINS = "domains"
CONF_WEB_USER = "web_user"
CONF_WEB_PASS = "web_pass"

# Providers
PROVIDER_STRATO = "STRATO"
PROVIDER_DUCKDNS = "DuckDNS"
PROVIDER_CLOUDFLARE = "Cloudflare"
PROVIDER_ALLINKL = "all-inkl.com"
PROVIDER_NOIP = "NoIP.com"

# Attributes (short, nice)
ATTR_IPV4 = "ipv4"
ATTR_IPV6 = "ipv6"
ATTR_LAST_UPDATE = "last_update"
ATTR_LAST_RESPONSE = "last_response"

UPDATE_PATH = "/dyndns-manager/"

# Dispatcher signals
SIGNAL_DOMAINS_UPDATED = "dyndns_manager_domains_updated"
SIGNAL_RESULTS_UPDATED = "dyndns_manager_results_updated"


class DynDNSStatus(StrEnum):
    """Canonical DynDNS status codes as enum (lowercase where applicable)."""
    S_911 = "911"            # provider/server error
    DONATOR = "!donator"
    ABUSE = "abuse"
    BADAGENT = "badagent"
    BADAUTH = "badauth"
    DNSERR = "dnserr"
    ERROR = "error"
    GOOD = "good"
    NOCHG = "nochg"
    NOTFQDN = "notfqdn"      # NOTE: use 'notfqdn' (not 'nofqdn')
    NOHOST = "nohost"
    NUMHOST = "numhost"
    OK = "ok"
    TIMEOUT = "timeout"
    UNKNOWN = "unknown"


# Enum options exported for entities (alphabetical for UI)
DYNDNS_STATE_OPTIONS: list[str] = sorted([s.value for s in DynDNSStatus])
