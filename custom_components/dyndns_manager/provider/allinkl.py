from __future__ import annotations
import aiohttp
from typing import Tuple

# All-inkl/Kasserver DynDNS endpoint (basic auth)
DYNDNS_URL = "https://dyndns.kasserver.com/"

class AllInklProvider:
    async def update_domain(self, session: aiohttp.ClientSession, credentials: dict, domain: str, ipv4: str | None, ipv6: str | None) -> Tuple[str, str, str, str | None, str | None]:
        user = credentials.get("allinkl_user")
        pw = credentials.get("allinkl_pass")
        if not user or not pw:
            raise ValueError("Missing all-inkl.com credentials")

        # One request per explicit IP (v4/v6). If neither provided, rely on server-detected IP.
        async def call_one(myip: str | None):
            params = {"hostname": domain}
            if myip:
                params["myip"] = myip
            async with session.get(DYNDNS_URL, params=params, auth=aiohttp.BasicAuth(user, pw)) as resp:
                text = await resp.text()
                return resp.status, text

        eff_v4 = ipv4
        eff_v6 = ipv6
        status_text = "error"
        dyndns2 = "911"
        text = ""

        # Try IPv4
        if ipv4 or (not ipv4 and not ipv6):
            code, text = await call_one(ipv4)
            if "good" in text or "nochg" in text:
                status_text = "ok"
                dyndns2 = text.strip()
            else:
                status_text = "error"
                dyndns2 = "911"

        # Try IPv6 if provided
        if ipv6:
            code6, text6 = await call_one(ipv6)
            text = (text + " | " + text6).strip(" |")
            if "good" in text6 or "nochg" in text6:
                status_text = "ok"
                dyndns2 = text6.strip()

        return status_text, dyndns2, text, eff_v4, eff_v6