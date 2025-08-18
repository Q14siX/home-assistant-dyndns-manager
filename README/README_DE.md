# DynDNS Manager

[![Version](https://img.shields.io/github/v/release/Q14siX/home-assistant-dyndns-manager)](https://github.com/Q14siX/home-assistant-dyndns-manager/releases)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Languages](https://img.shields.io/badge/languages-20-blue.svg)
![Status](https://img.shields.io/badge/status-stable-brightgreen.svg)
![Downloads](https://img.shields.io/github/downloads/Q14siX/home-assistant-dyndns-manager/total)

---

## 📌 Línguas / 语言 / 語言 / Jazyky / Sprog / Sprachen / Talen / Languages / Kielet / Langues / Nyelvek / Lingue / 言語 / Språk / Języki / Línguas / Языки / Idiomas / Språk / Diller

- 🇧🇷 [Português Brasileiro (pt-BR)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_PT-BR.md#portugues-brasileiro)
- 🇨🇳 [中文 (简体, zh-CN)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_ZH-CN.md#简体中文)
- 🇹🇼 [中文 (繁體, zh-TW)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_ZH-TW.md#繁體中文)
- 🇨🇿 [Čeština (cs)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_CS.md#czech)
- 🇩🇰 [Dansk (da)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_DA.md#dansk)
- 🇩🇪 [**Deutsch (de)**](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_DE.md#deutsch)
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

## Deutsch

[![Buy Me A Coffee](https://img.buymeacoffee.com/button-api/?text=Buy%20Stefan%20a%20tasty%20coffee&emoji=☕&slug=q14six&button_colour=FFDD00&font_colour=000000&font_family=Lato&outline_colour=000000&coffee_colour=ffffff)](https://buymeacoffee.com/q14six)

**DynDNS Manager** ist eine benutzerfreundliche [Home Assistant](https://www.home-assistant.io/) Integration, mit der Sie Ihre DynDNS-Provider direkt aus Home Assistant heraus verwalten und aktualisieren können.  
Die Integration unterstützt aktuell folgende Provider:

- **AllInkl**
- **Cloudflare**
- **DuckDNS**
- **NoIP**
- **Strato**

💡 Zusätzlich kann eine **Fritz!Box** so konfiguriert werden, dass sie ein Update an den DynDNS Manager sendet.

Die Integration bietet:
- Automatisches Aktualisieren Ihrer DynDNS-Einträge
- Einfacher Konfigurationsdialog über die Home Assistant Benutzeroberfläche (Config Flow)
- Unterstützung mehrerer Provider gleichzeitig
- Direkte manuelle Aktualisierung über Home Assistant Buttons
- Direkter Aufruf eines DynDNS-Updates per Home Assistant Service (für Automatisierungen und Skripte)

---

### 🚀 Installation

#### 🔹 Installation über HACS (empfohlen)

1. Öffnen Sie **HACS** in Ihrem Home Assistant.
2. Gehen Sie zu **Integrationen**.
3. Klicken Sie auf die **3 Punkte** oben rechts und wählen Sie **Benutzerdefiniertes Repository hinzufügen**.
4. Fügen Sie folgendes Repository hinzu:

   ```
   https://github.com/Q14siX/home-assistant-dyndns-manager
   ```

   Kategorie: **Integration**

5. Suchen Sie nun nach **DynDNS Manager** in HACS und installieren Sie es.
6. Starten Sie Home Assistant neu.

---

#### 🔹 Manuelle Installation

1. Laden Sie die aktuelle Version von [GitHub Releases](https://github.com/Q14siX/home-assistant-dyndns-manager/releases) herunter.
2. Entpacken Sie die ZIP-Datei.
3. Kopieren Sie den Ordner **`dyndns_manager`** aus `custom_components` in Ihren Home Assistant `custom_components`-Ordner:

   ```bash
   cp -r custom_components/dyndns_manager /config/custom_components/
   ```

4. Starten Sie Home Assistant neu.

---

### ⚙️ Einrichtung in Home Assistant

1. Gehen Sie in Home Assistant zu **Einstellungen → Geräte & Dienste**.
2. Klicken Sie auf **Integration hinzufügen**.
3. Suchen Sie nach **DynDNS Manager**.
4. Wählen Sie den gewünschten Provider (DuckDNS, Strato, Cloudflare, NoIP oder ALL-INKL) aus.
5. Geben Sie die erforderlichen Zugangsdaten / API-Keys ein.
6. Fertig! Ihre DynDNS-Einträge werden nun automatisch aktualisiert.

---

### 📄 Konfiguration

#### Unterstützte Provider & benötigte Daten

| Provider    | Benötigte Daten |
|-------------|----------------|
| ALL-INKL    | Benutzername, Passwort, Domain |
| Cloudflare  | API Token, Zone ID, Domain |
| DuckDNS     | API Token, Domain |
| NoIP        | Benutzername, Passwort, Domain |
| Strato      | Benutzername, Passwort, Domain |

Alle Eingaben erfolgen bequem über den **Config Flow** in der Home Assistant Oberfläche – keine `configuration.yaml`-Änderungen nötig.

---

### 📡 Fritz!Box Anbindung

Die Integration kann Updates auch von einer Fritz!Box empfangen.

Dazu in der Fritz!Box unter **Internet → Freigaben → Dynamic DNS** folgende URL eintragen:

```
http://<ha_host>:<ha_port>/dyndns-manager/?username=<username>&password=<pass>&ipv4=<ipaddr>&ipv6=<ip6addr>
```

- `<ha_host>` → Hostname oder IP-Adresse Ihres Home Assistant
- `<ha_port>` → Port von Home Assistant (Standard: 8123)
- `<username>` / `<pass>` → Zugangsdaten für den Webzugriff (siehe Einrichtungsassistenten)
- `<ipaddr>` / `<ip6addr>` → Platzhalter für die IPv4 und/oder IPv6

💡 **Hinweis:** In der Fritz!Box muss in der URL nur `<ha_host>` und `<ha_port>` angepasst werden. Alle anderen Werte (`<username>`, `<pass>`, `<ipaddr>`, `<ip6addr>`) werden von der Fritz!Box automatisch ersetzt, wenn Sie das Eingabeformular ausfüllen.

![FRITZ!BOX Eingabemaske](https://raw.githubusercontent.com/Q14siX/home-assistant-dyndns-manager/master/images/FRITZ!Box.png)

---

### 🔘 Funktionen in Home Assistant

- **Sensoren** → zeigen den aktuellen Status und die IP-Adresse an
- **Buttons** → ermöglichen eine manuelle Aktualisierung der IP
- **Service** → ermöglicht das direkte Ausführen eines DynDNS-Updates aus Automatisierungen oder Skripten

---

### 🛠 Entwicklung

1. Klonen Sie das Repository:
   ```bash
   git clone https://github.com/Q14siX/home-assistant-dyndns-manager.git
   ```
2. Erstellen Sie eine neue Provider-Datei im Ordner `custom_components/dyndns_manager/provider/`.
3. Implementieren Sie die Update-Logik entsprechend den anderen Providern.

---

### 📬 Fehler & Unterstützung

- **Issues melden:** [GitHub Issues](https://github.com/Q14siX/home-assistant-dyndns-manager/issues)
- **Dokumentation:** [GitHub Readme](https://github.com/Q14siX/home-assistant-dyndns-manager)

---

### 📜 Lizenz

Dieses Projekt steht unter der **MIT-Lizenz** – siehe [LICENSE](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/LICENSE) für Details.
