
from __future__ import annotations
import aiohttp
from typing import Tuple, Optional
from urllib.parse import quote

API_BASE = "https://api.cloudflare.com/client/v4"

class CloudflareProvider:
    async def update_domain(self, session: aiohttp.ClientSession, credentials: dict, domain: str, ipv4: Optional[str], ipv6: Optional[str]) -> Tuple[str, str, str, Optional[str], Optional[str]]:
        token = credentials.get("cf_api_token")
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

        zone_name = domain.split(".", 1)[1] if "." in domain else domain
        async with session.get(f"{API_BASE}/zones?name={quote(zone_name)}", headers=headers) as resp:
            z = await resp.json()
            if not z.get("success") or not z.get("result"):
                text = str(z)
                return "error", "911", text, ipv4, ipv6
            zone_id = z["result"][0]["id"]

        async def ensure_record(name: str, rtype: str, content: str):
            async with session.get(f"{API_BASE}/zones/{zone_id}/dns_records?type={rtype}&name={quote(name)}", headers=headers) as r:
                data = await r.json()
                if data.get("result"):
                    rec = data["result"][0]
                    rec_id = rec["id"]
                    async with session.put(f"{API_BASE}/zones/{zone_id}/dns_records/{rec_id}", headers=headers, json={"type": rtype, "name": name, "content": content, "ttl": 1}) as ur:
                        return await ur.json()
                else:
                    async with session.post(f"{API_BASE}/zones/{zone_id}/dns_records", headers=headers, json={"type": rtype, "name": name, "content": content, "ttl": 1}) as cr:
                        return await cr.json()

        results = []
        if ipv4:
            results.append(await ensure_record(domain, "A", ipv4))
        if ipv6:
            results.append(await ensure_record(domain, "AAAA", ipv6))

        ok = all(r.get("success") for r in results) if results else False
        text = str(results)
        if ok:
            dyndns2 = f"good {ipv4 or ipv6 or ''}".strip()
            return "ok", dyndns2, text, ipv4, ipv6
        else:
            return "error", "911", text, ipv4, ipv6
