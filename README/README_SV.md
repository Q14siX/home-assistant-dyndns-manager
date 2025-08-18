# DynDNS Manager

[![Version](https://img.shields.io/github/v/release/Q14siX/home-assistant-dyndns-manager)](https://github.com/Q14siX/home-assistant-dyndns-manager/releases)  
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
![Språk](https://img.shields.io/badge/languages-20-blue.svg)  
![Status](https://img.shields.io/badge/status-stable-brightgreen.svg)  
![Nedladdningar](https://img.shields.io/github/downloads/Q14siX/home-assistant-dyndns-manager/total)

---

## 📌 Línguas / 语言 / 語言 / Jazyky / Sprog / Sprachen / Talen / Languages / Kielet / Langues / Nyelvek / Lingue / 言語 / Språk / Języki / Línguas / Языки / Idiomas / Språk / Diller

- 🇧🇷 [Português Brasileiro (pt-BR)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_PT-BR.md#portugues-brasileiro)
- 🇨🇳 [中文 (简体, zh-CN)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_ZH-CN.md#简体中文)
- 🇹🇼 [中文 (繁體, zh-TW)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_ZH-TW.md#繁體中文)
- 🇨🇿 [Čeština (cs)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_CS.md#czech)
- 🇩🇰 [Dansk (da)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_DA.md#dansk)
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
- 🇸🇪 [**Svenska (sv)**](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_SV.md#svenska)
- 🇹🇷 [Türkçe (tr)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_TR.md#türkçe)

---

## Svenska

<a href="https://www.buymeacoffee.com/Q14siX" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

**DynDNS Manager** är en användarvänlig integration för [Home Assistant](https://www.home-assistant.io/) som låter dig hantera och uppdatera dina DynDNS-leverantörer direkt från Home Assistant.  
Integrationen stöder för närvarande följande leverantörer:

- **AllInkl**
- **Cloudflare**
- **DuckDNS**
- **NoIP**
- **Strato**

> [!NOTE]
> Dessutom kan en **Fritz!Box** konfigureras att skicka uppdateringar till DynDNS Manager.

Integrationen erbjuder:
- Automatisk uppdatering av dina DynDNS-poster
- Enkel konfigurationsguide via Home Assistants gränssnitt (Config Flow)
- Stöd för flera leverantörer samtidigt
- Direkt manuell uppdatering via knappar i Home Assistant
- Direkt körning av en DynDNS‑uppdatering via Home Assistant‑tjänsten (för automationer och skript)

---

### 🚀 Installation

#### 🔹 Installation via HACS (rekommenderas)

1. Öppna **HACS** i din Home Assistant.
2. Gå till **Integrationer**.
3. Klicka på **3 punkter** uppe till höger och välj **Lägg till anpassat repository**.
4. Lägg till följande repository:

   ```
   https://github.com/Q14siX/home-assistant-dyndns-manager
   ```

   Kategori: **Integration**

5. Sök efter **DynDNS Manager** i HACS och installera.
6. Starta om Home Assistant.

---

#### 🔹 Manuell installation

1. Ladda ner den senaste versionen från [GitHub Releases](https://github.com/Q14siX/home-assistant-dyndns-manager/releases).
2. Packa upp ZIP‑filen.
3. Kopiera mappen **`dyndns_manager`** från `custom_components` till din Home Assistant‑mapp `custom_components`:

   ```bash
   cp -r custom_components/dyndns_manager /config/custom_components/
   ```

4. Starta om Home Assistant.

---

### ⚙️ Konfiguration i Home Assistant

1. Gå i Home Assistant till **Inställningar → Enheter & tjänster**.
2. Klicka på **Lägg till integration**.
3. Sök efter **DynDNS Manager**.
4. Välj önskad leverantör (DuckDNS, Strato, Cloudflare, NoIP eller ALL-INKL).
5. Ange nödvändiga inloggningsuppgifter / API‑nycklar.
6. Klart! Dina DynDNS‑poster uppdateras nu automatiskt.

---

### 📄 Konfiguration

#### Stödda leverantörer och nödvändiga uppgifter

| Leverantör | Nödvändiga uppgifter |
|------------|----------------------|
| ALL-INKL   | Användarnamn, lösenord, domän |
| Cloudflare | API‑token, Zone ID, domän |
| DuckDNS    | API‑token, domän |
| NoIP       | Användarnamn, lösenord, domän |
| Strato     | Användarnamn, lösenord, domän |

All konfiguration görs enkelt via **Config Flow** i Home Assistant‑gränssnittet – inga ändringar i `configuration.yaml` behövs.

---

### 📡 Fritz!Box‑anslutning

Integrationen kan även ta emot uppdateringar från en Fritz!Box.

I Fritz!Box, under **Internet → Delningar → Dynamic DNS**, ange följande URL:

```
http://<ha_host>:<ha_port>/dyndns-manager/?username=<username>&password=<pass>&ipv4=<ipaddr>&ipv6=<ip6addr>
```

- `<ha_host>` → värdnamn eller IP‑adress till din Home Assistant
- `<ha_port>` → port för Home Assistant (standard: 8123)
- `<username>` / `<pass>` → inloggningsuppgifter för webbtillgång (se installationsguiden)
- `<ipaddr>` / `<ip6addr>` → platshållare för IPv4 och/eller IPv6

> [!TIP]
> I Fritz!Box behöver du bara ändra `<ha_host>` och `<ha_port>`. Övriga värden (`<username>`, `<pass>`, `<ipaddr>`, `<ip6addr>`) fylls i automatiskt av Fritz!Box när du skickar formuläret.

![FRITZ!BOX formulär](https://raw.githubusercontent.com/Q14siX/home-assistant-dyndns-manager/master/images/FRITZ!Box.png)

---

### 🔘 Funktioner i Home Assistant

- **Sensorer** → visar aktuell status och IP‑adress
- **Knappar** → möjliggör manuell IP‑uppdatering
- **Tjänst** → möjliggör att köra en DynDNS‑uppdatering direkt från automationer eller skript

---

### 🛠 Utveckling

1. Klona repo:t:
   ```bash
   git clone https://github.com/Q14siX/home-assistant-dyndns-manager.git
   ```
2. Skapa en ny leverantörsfil i mappen `custom_components/dyndns_manager/provider/`.
3. Implementera uppdateringslogiken i enlighet med de övriga leverantörerna.

---

### 📬 Fel & support

- **Rapportera problem:** [GitHub Issues](https://github.com/Q14siX/home-assistant-dyndns-manager/issues)  
- **Dokumentation:** [GitHub Readme](https://github.com/Q14siX/home-assistant-dyndns-manager)

---

### 📜 Licens

Detta projekt är licensierat under **MIT‑licensen** – se [LICENSE](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/LICENSE) för detaljer.
