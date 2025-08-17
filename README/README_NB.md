# DynDNS Manager

[![Versjon](https://img.shields.io/github/v/release/Q14siX/home-assistant-dyndns-manager)](https://github.com/Q14siX/home-assistant-dyndns-manager/releases)  
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
![Språk](https://img.shields.io/badge/languages-20-blue.svg)  
![Status](https://img.shields.io/badge/status-stable-brightgreen.svg)  
![Nedlastinger](https://img.shields.io/github/downloads/Q14siX/home-assistant-dyndns-manager/total)

---

## 📌 Línguas / 语言 / 語言 / Jazyky / Sprog / Sprachen / Talen / Languages / Kielet / Langues / Nyelvek / Lingue / 言語 / Språk / Języki / Línguas / Языки / Idiomas / Språk / Diller
- [Brazilian Portuguese (pt-BR)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_PT-BR.md#portugues-brasileiro)
- [Chinese (Simplified, zh-CN)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_ZH-CN.md#简体中文)
- [Chinese (Traditional, zh-TW)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_ZH-TW.md#繁體中文)
- [Czech (cs)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_CS.md#czech)
- [Danish (da)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_DA.md#dansk)
- [Deutsch (de)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_DE.md#deutsch)
- [Dutch (nl)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_NL.md#dutch)
- [English (en)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_EN.md#english)
- [Finnish (fi)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_FI.md#suomi)
- [French (fr)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_FR.md#français)
- [Hungarian (hu)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_HU.md#magyar)
- [Italian (it)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_IT.md#italiano)
- [Japanese (ja)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_JA.md#日本語)
- [**Norwegian (Bokmål, nb)**](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_NB.md#norsk)
- [Polish (pl)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_PL.md#polski)
- [Portuguese (pt)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_PT.md#português)
- [Russian (ru)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_RU.md#Русский)
- [Spanish (es)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_ES.md#español)
- [Swedish (sv)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_SV.md#svenska)
- [Turkish (tr)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_TR.md#türkçe)

---

## Norsk

[![Buy Me A Coffee](https://img.buymeacoffee.com/button-api/?text=Buy%20Stefan%20a%20tasty%20coffee&emoji=☕&slug=q14six&button_colour=FFDD00&font_colour=000000&font_family=Lato&outline_colour=000000&coffee_colour=ffffff)](https://buymeacoffee.com/q14six)

**DynDNS Manager** er en brukervennlig integrasjon for [Home Assistant](https://www.home-assistant.io/) som lar deg administrere og oppdatere DynDNS-leverandører direkte fra Home Assistant.  
Integrasjonen støtter for øyeblikket følgende leverandører:

- **AllInkl**
- **Cloudflare**
- **DuckDNS**
- **NoIP**
- **Strato**

💡 I tillegg kan en **Fritz!Box** konfigureres til å sende oppdateringer til DynDNS Manager.

Integrasjonen tilbyr:
- Automatisk oppdatering av DynDNS-poster
- Enkel konfigurasjonsveiviser via Home Assistant-grensesnittet (Config Flow)
- Støtte for flere leverandører samtidig
- Direkte manuell oppdatering via knapper i Home Assistant
- Direkte kjøring av en DynDNS-oppdatering via Home Assistant-tjenesten (for automatiseringer og skript)

---

### 🚀 Installasjon

#### 🔹 Installasjon via HACS (anbefalt)

1. Åpne **HACS** i Home Assistant.
2. Gå til **Integrasjoner**.
3. Klikk på **3 prikker** øverst til høyre og velg **Legg til egendefinert repository**.
4. Legg til følgende repository:

   ```
   https://github.com/Q14siX/home-assistant-dyndns-manager
   ```

   Kategori: **Integrasjon**

5. Søk etter **DynDNS Manager** i HACS og installer.
6. Start Home Assistant på nytt.

---

#### 🔹 Manuell installasjon

1. Last ned nyeste versjon fra [GitHub Releases](https://github.com/Q14siX/home-assistant-dyndns-manager/releases).
2. Pakk ut ZIP-filen.
3. Kopier mappen **`dyndns_manager`** fra `custom_components` til Home Assistant sin `custom_components`-mappe:

   ```bash
   cp -r custom_components/dyndns_manager /config/custom_components/
   ```

4. Start Home Assistant på nytt.

---

### ⚙️ Oppsett i Home Assistant

1. Gå i Home Assistant til **Innstillinger → Enheter og tjenester**.
2. Klikk **Legg til integrasjon**.
3. Søk etter **DynDNS Manager**.
4. Velg ønsket leverandør (DuckDNS, Strato, Cloudflare, NoIP eller ALL-INKL).
5. Oppgi nødvendige påloggingsdata / API-nøkler.
6. Ferdig! DynDNS-postene dine oppdateres nå automatisk.

---

### 📄 Konfigurasjon

#### Støttede leverandører og nødvendige data

| Leverandør | Nødvendige data |
|------------|-----------------|
| ALL-INKL   | Brukernavn, passord, domene |
| Cloudflare | API-token, Zone ID, domene |
| DuckDNS    | API-token, domene |
| NoIP       | Brukernavn, passord, domene |
| Strato     | Brukernavn, passord, domene |

All konfigurasjon gjøres enkelt via **Config Flow** i Home Assistant-grensesnittet – ingen endringer i `configuration.yaml` er nødvendig.

---

### 📡 Fritz!Box-tilkobling

Integrasjonen kan også motta oppdateringer fra en Fritz!Box.

I Fritz!Box under **Internet → Delinger → Dynamic DNS** angir du følgende URL:

```
http://<ha_host>:<ha_port>/dyndns-manager/?username=<username>&password=<pass>&ipv4=<ipaddr>&ipv6=<ip6addr>
```

- `<ha_host>` → vertsnavn eller IP-adresse til Home Assistant
- `<ha_port>` → port for Home Assistant (standard: 8123)
- `<username>` / `<pass>` → legitimasjon for nettilgang (se veiviseren for oppsett)
- `<ipaddr>` / `<ip6addr>` → plassholdere for IPv4 og/eller IPv6

💡 **Merk:** I Fritz!Box trenger du kun å endre `<ha_host>` og `<ha_port>`. Alle andre verdier (`<username>`, `<pass>`, `<ipaddr>`, `<ip6addr>`) fylles inn automatisk av Fritz!Box når du fyller ut skjemaet.

![FRITZ!BOX inntastingsskjema](https://raw.githubusercontent.com/Q14siX/home-assistant-dyndns-manager/master/images/FRITZ!Box.png)

---

### 🔘 Funksjoner i Home Assistant

- **Sensorer** → viser gjeldende status og IP-adresse
- **Knapper** → muliggjør manuell IP-oppdatering
- **Tjeneste** → muliggjør direkte kjøring av en DynDNS-oppdatering fra automatiseringer eller skript

---

### 🛠 Utvikling

1. Klon repoet:
   ```bash
   git clone https://github.com/Q14siX/home-assistant-dyndns-manager.git
   ```
2. Opprett en ny leverandørfil i mappen `custom_components/dyndns_manager/provider/`.
3. Implementer oppdateringslogikken etter mønster fra de andre leverandørene.

---

### 📬 Feil og support

- **Meld problemer:** [GitHub Issues](https://github.com/Q14siX/home-assistant-dyndns-manager/issues)  
- **Dokumentasjon:** [GitHub Readme](https://github.com/Q14siX/home-assistant-dyndns-manager)

---

### 📜 Lisens

Dette prosjektet er lisensiert under **MIT-lisensen** – se [LICENSE](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/LICENSE) for detaljer.
