
from __future__ import annotations
import aiohttp, re
from typing import Tuple, Optional
from yarl import URL

_ipv4 = re.compile(r"(?:\d{1,3}\.){3}\d{1,3}")
_ipv6 = re.compile(r"([0-9a-fA-F:]+:+)+[0-9a-fA-F]+")

def _extract_ips(text: str) -> tuple[Optional[str], Optional[str]]:
    v4 = _ipv4.search(text)
    v6 = _ipv6.search(text)
    return (v4.group(0) if v4 else None, v6.group(0) if v6 else None)

class StratoProvider:
    async def update_domain(self, session: aiohttp.ClientSession, credentials: dict, domain: str, ipv4: str | None, ipv6: str | None) -> Tuple[str, str, str, str | None, str | None]:
        user = credentials.get("strato_user")
        pwd = credentials.get("strato_pass")

        params = {"hostname": domain}
        if ipv4 and ipv6:
            params["myip"] = f"{ipv4},{ipv6}"
        elif ipv4:
            params["myip"] = ipv4
        elif ipv6:
            params["myip"] = ipv6

        url = URL("https://dyndns.strato.com/nic/update").with_query(params)

        async with session.get(str(url), auth=aiohttp.BasicAuth(user, pwd)) as resp:
            text = await resp.text()
            if text.startswith("good") or text.startswith("nochg"):
                status = "ok"
                dyndns2 = text.strip().split()[0]
            elif text.startswith("badauth"):
                status = "error"
                dyndns2 = "badauth"
            else:
                status = "error"
                dyndns2 = text.strip().split()[0]
            v4, v6 = _extract_ips(text)
            # Prefer parsed values; fall back to provided
            return status, dyndns2, text, v4 or ipv4, v6 or ipv6
