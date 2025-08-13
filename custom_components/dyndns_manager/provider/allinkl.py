from __future__ import annotations
import aiohttp
from typing import Tuple, Optional
from yarl import URL

class AllInklProvider:
    async def update_domain(self, session: aiohttp.ClientSession, credentials: dict, domain: str, ipv4: str | None, ipv6: str | None) -> Tuple[str, str, str, str | None, str | None]:
        user = credentials.get("allinkl_user")
        pwd = credentials.get("allinkl_pass")
        results = []
        eff_v4: Optional[str] = None
        eff_v6: Optional[str] = None

        async def update_one(ip: str):
            url = URL("https://dyndns.kasserver.com/").with_query({"hostname": domain, "myip": ip})
            async with session.get(str(url), auth=aiohttp.BasicAuth(user, pwd), headers={"User-Agent": "HomeAssistant-DynDNS-Manager"}) as resp:
                text = (await resp.text()).strip()
                return text

        if ipv4:
            t = await update_one(ipv4)
            results.append(("v4", t))
            if t.startswith("good") or t.startswith("nochg"):
                eff_v4 = ipv4
        if ipv6:
            t = await update_one(ipv6)
            results.append(("v6", t))
            if t.startswith("good") or t.startswith("nochg"):
                eff_v6 = ipv6

        texts = [f"{k}:{v}" for k,v in results] or ["no-op"]
        joined = " | ".join(texts)
        if results and all((t.startswith("good") or t.startswith("nochg")) for _, t in results):
            dyndns2 = "good" if any(t.startswith("good") for _, t in results) else "nochg"
            return "ok", dyndns2, joined, eff_v4 or ipv4, eff_v6 or ipv6
        elif results:
            for _, t in results:
                tok = (t.split()[0] if t else "error")
                if tok not in ("good", "nochg"):
                    return "error", tok, joined, eff_v4 or ipv4, eff_v6 or ipv6
        return "error", "911", joined, eff_v4 or ipv4, eff_v6 or ipv6
