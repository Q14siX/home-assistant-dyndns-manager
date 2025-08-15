
from __future__ import annotations
import aiohttp
from typing import Tuple

def _classify(ip: str | None):
    if not ip:
        return None
    return "v6" if ":" in ip else "v4"

class DuckDNSProvider:
    async def update_domain(self, session: aiohttp.ClientSession, credentials: dict, domain: str, ipv4: str | None, ipv6: str | None) -> Tuple[str, str, str, str | None, str | None]:
        token = credentials.get("duckdns_token")
        params = {"domains": domain, "token": token}
        if ipv4:
            params["ip"] = ipv4
        if ipv6:
            params["ipv6"] = ipv6

        async with session.get("https://www.duckdns.org/update", params=params) as resp:
            text = await resp.text()
            if "OK" in text.upper():
                # DuckDNS doesn't echo ip; prefer the one we sent
                eff_v4 = ipv4 if _classify(ipv4) == "v4" else None
                eff_v6 = ipv6 if _classify(ipv6) == "v6" else None
                dyndns2 = f"good {(eff_v4 or eff_v6 or '').strip()}".strip()
                status = "ok"
            else:
                dyndns2 = "911"
                status = "error"
            return status, dyndns2, text, eff_v4 if 'eff_v4' in locals() else None, eff_v6 if 'eff_v6' in locals() else None
