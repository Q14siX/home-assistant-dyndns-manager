
from __future__ import annotations

from .duckdns import DuckDNSProvider
from .strato import StratoProvider
from .cloudflare import CloudflareProvider

def get_provider(name: str):
    if name == "DuckDNS":
        return DuckDNSProvider()
    if name == "STRATO":
        return StratoProvider()
    if name == "Cloudflare":
        return CloudflareProvider()
    raise ValueError(f"Unknown provider: {name}")
