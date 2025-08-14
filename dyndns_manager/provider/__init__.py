
from __future__ import annotations

from .duckdns import DuckDNSProvider
from .strato import StratoProvider
from .cloudflare import CloudflareProvider
from .noip import NoIPProvider
from .allinkl import AllInklProvider

def get_provider(name: str):
    if name == "DuckDNS":
        return DuckDNSProvider()
    if name == "STRATO":
        return StratoProvider()
    if name == "Cloudflare":
        return CloudflareProvider()
    if name == "NoIP.com":
        return NoIPProvider()
    if name == "all-inkl.com":
        return AllInklProvider()
    raise ValueError(f"Unknown provider: {name}")
