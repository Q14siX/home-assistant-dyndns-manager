# DynDNS Manager

[![Version](https://img.shields.io/github/v/release/Q14siX/home-assistant-dyndns-manager)](https://github.com/Q14siX/home-assistant-dyndns-manager/releases)  
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
![Sprog](https://img.shields.io/badge/languages-20-blue.svg)  
![Status](https://img.shields.io/badge/status-stable-brightgreen.svg)  
![Downloads](https://img.shields.io/github/downloads/Q14siX/home-assistant-dyndns-manager/total)

---

## 📌 Línguas / 语言 / 語言 / Jazyky / Sprog / Sprachen / Talen / Languages / Kielet / Langues / Nyelvek / Lingue / 言語 / Språk / Języki / Línguas / Языки / Idiomas / Språk / Diller

- 🇧🇷 [Português Brasileiro (pt-BR)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_PT-BR.md#portugues-brasileiro)
- 🇨🇳 [中文 (简体, zh-CN)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_ZH-CN.md#简体中文)
- 🇹🇼 [中文 (繁體, zh-TW)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_ZH-TW.md#繁體中文)
- 🇨🇿 [Čeština (cs)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_CS.md#czech)
- 🇩🇰 [**Dansk (da)**](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_DA.md#dansk)
- 🇩🇪 [Deutsch (de)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_DE.md#deutsch)
- 🇳🇱 [Nederlands (nl)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_NL.md#dutch)
- 🇬🇧 [English (en)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_EN.md#english)
- 🇫🇮 [Suomi (fi)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_FI.md#suomi)
- 🇫🇷 [Français (fr)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_FR.md#français)
- 🇭🇺 [Magyar (hu)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_HU.md#magyar)
- 🇮🇹 [Italiano (it)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_IT.md#italiano)
- 🇯🇵 [日本語 (ja)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_JA.md#日本語)
- 🇳🇴 [Norsk bokmål (nb)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_NB.md#norsk)
- 🇵🇱 [Polski (pl)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_PL.md#polski)
- 🇵🇹 [Português (pt)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_PT.md#português)
- 🇷🇺 [Русский (ru)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_RU.md#Русский)
- 🇪🇸 [Español (es)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_ES.md#español)
- 🇸🇪 [Svenska (sv)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_SV.md#svenska)
- 🇹🇷 [Türkçe (tr)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_TR.md#türkçe)

---

## Dansk

[![Buy Me A Coffee](https://img.buymeacoffee.com/button-api/?text=Buy%20Stefan%20a%20tasty%20coffee&emoji=☕&slug=q14six&button_colour=FFDD00&font_colour=000000&font_family=Lato&outline_colour=000000&coffee_colour=ffffff)](https://buymeacoffee.com/q14six)

**DynDNS Manager** er en brugervenlig integration til [Home Assistant](https://www.home-assistant.io/), som giver dig mulighed for at administrere og opdatere dine DynDNS-udbydere direkte fra Home Assistant.  
Integrationen understøtter i øjeblikket følgende udbydere:

- **AllInkl**
- **Cloudflare**
- **DuckDNS**
- **NoIP**
- **Strato**

💡 Derudover kan en **Fritz!Box** konfigureres til at sende opdateringer til DynDNS Manager.

Integrationen tilbyder:
- Automatisk opdatering af dine DynDNS-poster
- Enkel konfigurationsdialog via Home Assistant-brugerfladen (Config Flow)
- Understøttelse af flere udbydere samtidig
- Direkte manuel opdatering via Home Assistant-knapper
- Direkte udførelse af en DynDNS-opdatering via Home Assistant-tjeneste (til automatiseringer og scripts)

---

### 🚀 Installation

#### 🔹 Installation via HACS (anbefalet)

1. Åbn **HACS** i din Home Assistant.
2. Gå til **Integrationer**.
3. Klik på **3 prikker** øverst til højre og vælg **Tilføj brugerdefineret repository**.
4. Tilføj følgende repository:

   ```
   https://github.com/Q14siX/home-assistant-dyndns-manager
   ```

   Kategori: **Integration**

5. Søg nu efter **DynDNS Manager** i HACS og installer den.
6. Genstart Home Assistant.

---

#### 🔹 Manuel installation

1. Download den nyeste version fra [GitHub Releases](https://github.com/Q14siX/home-assistant-dyndns-manager/releases).
2. Udpak ZIP-filen.
3. Kopiér mappen **`dyndns_manager`** fra `custom_components` til din Home Assistant `custom_components`-mappe:

   ```bash
   cp -r custom_components/dyndns_manager /config/custom_components/
   ```

4. Genstart Home Assistant.

---

### ⚙️ Opsætning i Home Assistant

1. Gå i Home Assistant til **Indstillinger → Enheder & tjenester**.
2. Klik på **Tilføj integration**.
3. Søg efter **DynDNS Manager**.
4. Vælg den ønskede udbyder (DuckDNS, Strato, Cloudflare, NoIP eller ALL-INKL).
5. Indtast de nødvendige legitimationsoplysninger / API-nøgler.
6. Færdig! Dine DynDNS-poster vil nu blive opdateret automatisk.

---

### 📄 Konfiguration

#### Understøttede udbydere & nødvendige data

| Udbyder    | Nødvendige data |
|------------|-----------------|
| ALL-INKL   | Brugernavn, adgangskode, domæne |
| Cloudflare | API-token, Zone ID, domæne |
| DuckDNS    | API-token, domæne |
| NoIP       | Brugernavn, adgangskode, domæne |
| Strato     | Brugernavn, adgangskode, domæne |

Alle oplysninger indtastes nemt via **Config Flow** i Home Assistant-grænsefladen – ingen ændringer i `configuration.yaml` er nødvendige.

---

### 📡 Fritz!Box integration

Integrationen kan også modtage opdateringer fra en Fritz!Box.

I Fritz!Box under **Internet → Frigivelser → Dynamic DNS** indtastes følgende URL:

```
http://<ha_host>:<ha_port>/dyndns-manager/?username=<username>&password=<pass>&ipv4=<ipaddr>&ipv6=<ip6addr>
```

- `<ha_host>` → Hostnavn eller IP-adresse på din Home Assistant
- `<ha_port>` → Port for Home Assistant (standard: 8123)
- `<username>` / `<pass>` → legitimationsoplysninger til webadgang (se opsætningsguiden)
- `<ipaddr>` / `<ip6addr>` → pladsholdere for IPv4 og/eller IPv6

💡 **Bemærk:** I Fritz!Box skal du kun ændre `<ha_host>` og `<ha_port>`. Alle andre værdier (`<username>`, `<pass>`, `<ipaddr>`, `<ip6addr>`) udfyldes automatisk af Fritz!Box, når du indtaster oplysningerne i formularen.

![FRITZ!BOX inputformular](https://raw.githubusercontent.com/Q14siX/home-assistant-dyndns-manager/master/images/FRITZ!Box.png)

---

### 🔘 Funktioner i Home Assistant

- **Sensorer** → viser den aktuelle status og IP-adresse
- **Knapper** → giver mulighed for manuel opdatering af IP
- **Tjeneste** → gør det muligt at udføre en DynDNS-opdatering direkte fra automatiseringer eller scripts

---

### 🛠 Udvikling

1. Klon repositoryet:
   ```bash
   git clone https://github.com/Q14siX/home-assistant-dyndns-manager.git
   ```
2. Opret en ny udbyderfil i mappen `custom_components/dyndns_manager/provider/`.
3. Implementer opdateringslogikken i henhold til de andre udbydere.

---

### 📬 Fejl & support

- **Rapporter problemer:** [GitHub Issues](https://github.com/Q14siX/home-assistant-dyndns-manager/issues)  
- **Dokumentation:** [GitHub Readme](https://github.com/Q14siX/home-assistant-dyndns-manager)

---

### 📜 Licens

Dette projekt er licenseret under **MIT-licensen** – se [LICENSE](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/LICENSE) for detaljer.
