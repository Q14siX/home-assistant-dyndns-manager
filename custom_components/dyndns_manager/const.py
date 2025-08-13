
DOMAIN = "dyndns_manager"

CONF_PROVIDER = "provider"
CONF_DOMAINS = "domains"
CONF_WEB_USER = "web_user"
CONF_WEB_PASS = "web_pass"

# Providers
PROVIDER_STRATO = "STRATO"
PROVIDER_DUCKDNS = "DuckDNS"
PROVIDER_CLOUDFLARE = "Cloudflare"
PROVIDER_NOIP = "NoIP"
PROVIDER_ALLINKL = "ALL-INKL"

# Attributes (short, nice)
ATTR_LAST_UPDATE = "aktualisiert"
ATTR_IPV4 = "ipv4"
ATTR_IPV6 = "ipv6"
ATTR_LAST_RESPONSE = "antwort"

UPDATE_PATH = "/dyndns-manager/"

# Dispatcher signals
SIGNAL_DOMAINS_UPDATED = "dyndns_manager_domains_updated"
SIGNAL_RESULTS_UPDATED = "dyndns_manager_results_updated"
