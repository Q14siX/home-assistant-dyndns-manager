# DynDNS Manager

[![Versie](https://img.shields.io/github/v/release/Q14siX/home-assistant-dyndns-manager)](https://github.com/Q14siX/home-assistant-dyndns-manager/releases)  
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
![Talen](https://img.shields.io/badge/languages-20-blue.svg)  
![Status](https://img.shields.io/badge/status-stable-brightgreen.svg)  
![Downloads](https://img.shields.io/github/downloads/Q14siX/home-assistant-dyndns-manager/total)

---

[![Buy Me A Coffee](https://img.buymeacoffee.com/button-api/?text=Koop%20Stefan%20een%20lekkere%20koffie&emoji=☕&slug=q14six&button_colour=FFDD00&font_colour=000000&font_family=Lato&outline_colour=000000&coffee_colour=ffffff)](https://buymeacoffee.com/q14six)

---

## 📌 Línguas / 语言 / 語言 / Jazyky / Sprog / Sprachen / Talen / Languages / Kielet / Langues / Nyelvek / Lingue / 言語 / Språk / Języki / Línguas / Языки / Idiomas / Språk / Diller
- [Brazilian Portuguese (pt-BR)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_PT-BR.md#portugues-brasileiro)
- [Chinese (Simplified, zh-CN)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_ZH-CN.md#简体中文)
- [Chinese (Traditional, zh-TW)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_ZH-TW.md#繁體中文)
- [Czech (cs)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_CS.md#czech)
- [Danish (da)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_DA.md#dansk)
- [Deutsch (de)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_DE.md#deutsch)
- [**Dutch (nl)**](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_NL.md#dutch)
- [English (en)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_EN.md#english)
- [Finnish (fi)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_FI.md#suomi)
- [French (fr)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_FR.md#français)
- [Hungarian (hu)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_HU.md#magyar)
- [Italian (it)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_IT.md#italiano)
- [Japanese (ja)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_JA.md#日本語)
- [Norwegian (Bokmål, nb)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_NB.md#norsk)
- [Polish (pl)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_PL.md#polski)
- [Portuguese (pt)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_PT.md#português)
- [Russian (ru)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_RU.md#Русский)
- [Spanish (es)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_ES.md#español)
- [Swedish (sv)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_SV.md#svenska)
- [Turkish (tr)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_TR.md#türkçe)

---

## Dutch

**DynDNS Manager** is een gebruiksvriendelijke integratie voor [Home Assistant](https://www.home-assistant.io/) waarmee je jouw DynDNS-providers rechtstreeks vanuit Home Assistant kunt beheren en bijwerken.  
De integratie ondersteunt momenteel de volgende providers:

- **AllInkl**
- **Cloudflare**
- **DuckDNS**
- **NoIP**
- **Strato**

💡 Bovendien kan een **Fritz!Box** worden geconfigureerd om updates naar de DynDNS Manager te sturen.

De integratie biedt:
- Automatische updates van je DynDNS-records
- Eenvoudige configuratiedialoog via de Home Assistant-interface (Config Flow)
- Ondersteuning voor meerdere providers tegelijk
- Directe handmatige updates via Home Assistant-knoppen
- Direct uitvoeren van een DynDNS-update via de Home Assistant-service (voor automatiseringen en scripts)

---

### 🚀 Installatie

#### 🔹 Installatie via HACS (aanbevolen)

1. Open **HACS** in je Home Assistant.
2. Ga naar **Integraties**.
3. Klik op de **3 puntjes** rechtsboven en kies **Aangepaste repository toevoegen**.
4. Voeg de volgende repository toe:

   ```
   https://github.com/Q14siX/home-assistant-dyndns-manager
   ```

   Categorie: **Integratie**

5. Zoek nu naar **DynDNS Manager** in HACS en installeer het.
6. Herstart Home Assistant.

---

#### 🔹 Handmatige installatie

1. Download de nieuwste versie van [GitHub Releases](https://github.com/Q14siX/home-assistant-dyndns-manager/releases).
2. Pak het ZIP-bestand uit.
3. Kopieer de map **`dyndns_manager`** uit `custom_components` naar je Home Assistant `custom_components`-map:

   ```bash
   cp -r custom_components/dyndns_manager /config/custom_components/
   ```

4. Herstart Home Assistant.

---

### ⚙️ Configuratie in Home Assistant

1. Ga in Home Assistant naar **Instellingen → Apparaten & diensten**.
2. Klik op **Integratie toevoegen**.
3. Zoek naar **DynDNS Manager**.
4. Selecteer de gewenste provider (DuckDNS, Strato, Cloudflare, NoIP of ALL-INKL).
5. Voer de vereiste inloggegevens / API-sleutels in.
6. Klaar! Je DynDNS-records worden nu automatisch bijgewerkt.

---

### 📄 Configuratie

#### Ondersteunde providers & benodigde gegevens

| Provider    | Benodigde gegevens |
|-------------|-------------------|
| ALL-INKL    | Gebruikersnaam, wachtwoord, domein |
| Cloudflare  | API-token, Zone ID, domein |
| DuckDNS     | API-token, domein |
| NoIP        | Gebruikersnaam, wachtwoord, domein |
| Strato      | Gebruikersnaam, wachtwoord, domein |

Alle invoer gebeurt eenvoudig via **Config Flow** in de Home Assistant-interface – geen wijzigingen in `configuration.yaml` nodig.

---

### 📡 Fritz!Box integratie

De integratie kan ook updates van een Fritz!Box ontvangen.

Voer in Fritz!Box onder **Internet → Toegang → Dynamic DNS** de volgende URL in:

```
http://<ha_host>:<ha_port>/dyndns-manager/?username=<username>&password=<pass>&ipv4=<ipaddr>&ipv6=<ip6addr>
```

- `<ha_host>` → Hostnaam of IP-adres van je Home Assistant
- `<ha_port>` → Poort van Home Assistant (standaard: 8123)
- `<username>` / `<pass>` → inloggegevens voor webtoegang (zie installatie-assistent)
- `<ipaddr>` / `<ip6addr>` → placeholders voor IPv4 en/of IPv6

💡 **Opmerking:** In Fritz!Box hoef je alleen `<ha_host>` en `<ha_port>` aan te passen. Alle andere waarden (`<username>`, `<pass>`, `<ipaddr>`, `<ip6addr>`) worden automatisch door Fritz!Box ingevuld wanneer je het formulier invult.

![FRITZ!BOX invoerformulier](https://raw.githubusercontent.com/Q14siX/home-assistant-dyndns-manager/master/images/FRITZ!Box.png)

---

### 🔘 Functies in Home Assistant

- **Sensoren** → tonen de actuele status en het IP-adres
- **Knoppen** → maken handmatige IP-updates mogelijk
- **Service** → maakt het mogelijk om een DynDNS-update direct uit te voeren vanuit automatiseringen of scripts

---

### 🛠 Ontwikkeling

1. Clone de repository:
   ```bash
   git clone https://github.com/Q14siX/home-assistant-dyndns-manager.git
   ```
2. Maak een nieuw providerbestand aan in de map `custom_components/dyndns_manager/provider/`.
3. Implementeer de update-logica volgens de andere providers.

---

### 📬 Fouten & ondersteuning

- **Problemen melden:** [GitHub Issues](https://github.com/Q14siX/home-assistant-dyndns-manager/issues)  
- **Documentatie:** [GitHub Readme](https://github.com/Q14siX/home-assistant-dyndns-manager)

---

### 📜 Licentie

Dit project valt onder de **MIT-licentie** – zie [LICENSE](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/LICENSE) voor details.
