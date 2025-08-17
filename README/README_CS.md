# DynDNS Manager

[![Verze](https://img.shields.io/github/v/release/Q14siX/home-assistant-dyndns-manager)](https://github.com/Q14siX/home-assistant-dyndns-manager/releases)  
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
![Jazyky](https://img.shields.io/badge/languages-20-blue.svg)  
![Stav](https://img.shields.io/badge/status-stable-brightgreen.svg)  
![Stažení](https://img.shields.io/github/downloads/Q14siX/home-assistant-dyndns-manager/total)

---

## 📌 Línguas / 语言 / 語言 / Jazyky / Sprog / Sprachen / Talen / Languages / Kielet / Langues / Nyelvek / Lingue / 言語 / Språk / Języki / Línguas / Языки / Idiomas / Språk / Diller
- [Brazilian Portuguese (pt-BR)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_PT-BR.md#portugues-brasileiro)
- Chinese (Simplified, zh-CN)
- Chinese (Traditional, zh-TW)
- [**Czech (cs)**](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_CS.md#czech)
- [Danish (da)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_DA.md#dansk)
- [Deutsch (de)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_DE.md#deutsch)
- [Dutch (nl)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_NL.md#dutch)
- [English (en)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_EN.md#english)
- [Finnish (fi)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_FI.md#suomi)
- [French (fr)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_FR.md#français)
- [Hungarian (hu)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_HU.md#magyar)
- [Italian (it)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_IT.md#italiano)
- [Japanese (ja)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_JA.md#日本語)
- [Norwegian (Bokmål, nb)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_NB.md#norsk)
- [Polish (pl)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_PL.md#polski)
- [Portuguese (pt)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_PT.md#português)
- [Russian (ru)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_RU.md#pусский)
- [Spanish (es)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_ES.md#español)
- [Swedish (sv)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_SV.md#svenska)
- [Turkish (tr)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_TR.md#türkçe)

---

## Czech

**DynDNS Manager** je uživatelsky přívětivá integrace pro [Home Assistant](https://www.home-assistant.io/), která vám umožní spravovat a aktualizovat vaše DynDNS poskytovatele přímo z Home Assistant.  
Integrace v současnosti podporuje následující poskytovatele:

- **AllInkl**
- **Cloudflare**
- **DuckDNS**
- **NoIP**
- **Strato**

💡 Navíc lze nakonfigurovat **Fritz!Box** tak, aby odesílal aktualizace do DynDNS Manageru.

Integrace nabízí:
- Automatickou aktualizaci vašich DynDNS záznamů
- Jednoduchý konfigurační dialog v rozhraní Home Assistant (Config Flow)
- Podporu více poskytovatelů současně
- Přímou manuální aktualizaci přes tlačítka v Home Assistant
- Přímé vyvolání aktualizace DynDNS pomocí služby Home Assistant (pro automatizace a skripty)

---

### 🚀 Instalace

#### 🔹 Instalace přes HACS (doporučeno)

1. Otevřete **HACS** ve vašem Home Assistant.
2. Přejděte na **Integrace**.
3. Klikněte na **3 tečky** vpravo nahoře a vyberte **Přidat vlastní repozitář**.
4. Přidejte následující repozitář:

   ```
   https://github.com/Q14siX/home-assistant-dyndns-manager
   ```

   Kategorie: **Integrace**

5. Vyhledejte **DynDNS Manager** v HACS a nainstalujte jej.
6. Restartujte Home Assistant.

---

#### 🔹 Ruční instalace

1. Stáhněte si aktuální verzi z [GitHub Releases](https://github.com/Q14siX/home-assistant-dyndns-manager/releases).
2. Rozbalte ZIP soubor.
3. Zkopírujte složku **`dyndns_manager`** z `custom_components` do vašeho Home Assistant `custom_components` adresáře:

   ```bash
   cp -r custom_components/dyndns_manager /config/custom_components/
   ```

4. Restartujte Home Assistant.

---

### ⚙️ Nastavení v Home Assistant

1. V Home Assistant jděte na **Nastavení → Zařízení & služby**.
2. Klikněte na **Přidat integraci**.
3. Vyhledejte **DynDNS Manager**.
4. Vyberte požadovaného poskytovatele (DuckDNS, Strato, Cloudflare, NoIP nebo ALL-INKL).
5. Zadejte požadované přihlašovací údaje / API klíče.
6. Hotovo! Vaše DynDNS záznamy se nyní budou automaticky aktualizovat.

---

### 📄 Konfigurace

#### Podporovaní poskytovatelé & potřebné údaje

| Poskytovatel | Potřebné údaje |
|--------------|----------------|
| ALL-INKL     | Uživatelské jméno, heslo, doména |
| Cloudflare   | API token, Zone ID, doména |
| DuckDNS      | API token, doména |
| NoIP         | Uživatelské jméno, heslo, doména |
| Strato       | Uživatelské jméno, heslo, doména |

Všechny údaje se zadávají pohodlně přes **Config Flow** v rozhraní Home Assistant – není třeba měnit `configuration.yaml`.

---

### 📡 Připojení Fritz!Box

Integrace může přijímat aktualizace i z Fritz!Boxu.

V Fritz!Boxu v části **Internet → Sdílení → Dynamic DNS** zadejte následující URL:

```
http://<ha_host>:<ha_port>/dyndns-manager/?username=<username>&password=<pass>&ipv4=<ipaddr>&ipv6=<ip6addr>
```

- `<ha_host>` → Hostname nebo IP adresa vašeho Home Assistant
- `<ha_port>` → Port Home Assistant (výchozí: 8123)
- `<username>` / `<pass>` → přihlašovací údaje pro webový přístup (viz průvodce nastavením)
- `<ipaddr>` / `<ip6addr>` → zástupné hodnoty pro IPv4 a/nebo IPv6

💡 **Poznámka:** V Fritz!Boxu stačí změnit pouze `<ha_host>` a `<ha_port>`. Ostatní hodnoty (`<username>`, `<pass>`, `<ipaddr>`, `<ip6addr>`) Fritz!Box doplní automaticky při vyplnění formuláře.

![FRITZ!BOX vstupní formulář](https://raw.githubusercontent.com/Q14siX/home-assistant-dyndns-manager/master/images/FRITZ!Box.png)

---

### 🔘 Funkce v Home Assistant

- **Senzory** → zobrazují aktuální stav a IP adresu
- **Tlačítka** → umožňují ruční aktualizaci IP
- **Služba** → umožňuje přímé spuštění DynDNS aktualizace z automatizací nebo skriptů

---

### 🛠 Vývoj

1. Naklonujte repozitář:
   ```bash
   git clone https://github.com/Q14siX/home-assistant-dyndns-manager.git
   ```
2. Vytvořte nový soubor poskytovatele ve složce `custom_components/dyndns_manager/provider/`.
3. Implementujte logiku aktualizace podle ostatních poskytovatelů.

---

### 📬 Chyby & podpora

- **Nahlašování problémů:** [GitHub Issues](https://github.com/Q14siX/home-assistant-dyndns-manager/issues)  
- **Dokumentace:** [GitHub Readme](https://github.com/Q14siX/home-assistant-dyndns-manager)

---

### 📜 Licence

Tento projekt je pod **MIT licencí** – viz [LICENSE](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/LICENSE) pro podrobnosti.
