# DynDNS Manager

[![Version](https://img.shields.io/github/v/release/Q14siX/home-assistant-dyndns-manager)](https://github.com/Q14siX/home-assistant-dyndns-manager/releases)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Languages](https://img.shields.io/badge/languages-43-blue.svg)
![Status](https://img.shields.io/badge/status-stable-brightgreen.svg)
![Downloads](https://img.shields.io/github/downloads/Q14siX/home-assistant-dyndns-manager/total)

---
## 📌 Sprachen / Languages
- [Deutsch](#deutsch)
- [English](#english)
- Afrikaans
- Arabic
- Bulgarian
- Catalan
- Czech
- Danish
- Greek
- Spanish
- Estonian
- Finnish
- French
- Hebrew
- Hindi
- Croatian
- Hungarian
- Indonesian
- Icelandic
- Italian
- Japanese
- Georgian
- Korean
- Lithuanian
- Latvian
- Norwegian Bokmål
- Dutch
- Polish
- Portuguese (Brazil)
- Portuguese (Portugal)
- Romanian
- Russian
- Slovak
- Slovenian
- Serbian
- Swedish
- Thai
- Turkish
- Ukrainian
- Urdu
- Vietnamese
- Chinese (Simplified)
- Chinese (Traditional)
---

## Deutsch

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

Dieses Projekt steht unter der **MIT-Lizenz** – siehe [LICENSE](LICENSE) für Details.

---

## English

**DynDNS Manager** is a user-friendly [Home Assistant](https://www.home-assistant.io/) integration that allows you to manage and update your DynDNS providers directly from Home Assistant.  
Currently supported providers:

- **AllInkl**
- **Cloudflare**
- **DuckDNS**
- **NoIP**
- **Strato**

💡 Additionally, a **Fritz!Box** can be configured to send updates to the DynDNS Manager.

Features:
- Automatic updating of your DynDNS records
- Easy configuration dialog through the Home Assistant UI (Config Flow)
- Support for multiple providers simultaneously
- Direct manual update via Home Assistant buttons
- Direct execution of a DynDNS update via Home Assistant service (for automations and scripts)

---

### 🚀 Installation

#### 🔹 Installation via HACS (recommended)

1. Open **HACS** in your Home Assistant.
2. Go to **Integrations**.
3. Click on the **3 dots** in the top right corner and select **Custom repositories**.
4. Add the following repository:

   ```
   https://github.com/Q14siX/home-assistant-dyndns-manager
   ```

   Category: **Integration**

5. Search for **DynDNS Manager** in HACS and install it.
6. Restart Home Assistant.

---

#### 🔹 Manual Installation

1. Download the latest version from [GitHub Releases](https://github.com/Q14siX/home-assistant-dyndns-manager/releases).
2. Extract the ZIP file.
3. Copy the folder **`dyndns_manager`** from `custom_components` to your Home Assistant `custom_components` directory:

   ```bash
   cp -r custom_components/dyndns_manager /config/custom_components/
   ```

4. Restart Home Assistant.

---

### ⚙️ Setup in Home Assistant

1. Go to **Settings → Devices & Services** in Home Assistant.
2. Click **Add Integration**.
3. Search for **DynDNS Manager**.
4. Select the desired provider (DuckDNS, Strato, Cloudflare, NoIP, or ALL-INKL).
5. Enter the required credentials / API keys.
6. Done! Your DynDNS entries will now be updated automatically.

---

### 📄 Configuration

#### Supported providers & required data

| Provider    | Required Data |
|-------------|---------------|
| ALL-INKL    | Username, Password, Domain |
| Cloudflare  | API Token, Zone ID, Domain |
| DuckDNS     | API Token, Domain |
| NoIP        | Username, Password, Domain |
| Strato      | Username, Password, Domain |

All input is done conveniently via the **Config Flow** in the Home Assistant UI – no `configuration.yaml` changes needed.

---

### 📡 Fritz!Box Integration

The integration can also receive updates from a Fritz!Box.

In the Fritz!Box, go to **Internet → Permit Access → Dynamic DNS** and enter the following URL:

```
http://<ha_host>:<ha_port>/dyndns-manager/?username=<username>&password=<pass>&ipv4=<ipaddr>&ipv6=<ip6addr>
```

- `<ha_host>` → Hostname or IP address of your Home Assistant
- `<ha_port>` → Home Assistant port (default: 8123)
- `<username>` / `<pass>` → Web access credentials (see setup wizard)
- `<ipaddr>` / `<ip6addr>` → Placeholders for IPv4 and/or IPv6

💡 **Note:** In the Fritz!Box, only `<ha_host>` and `<ha_port>` need to be changed in the URL. All other values (`<username>`, `<pass>`, `<ipaddr>`, `<ip6addr>`) are automatically replaced by the Fritz!Box when you fill in the input form.

![FRITZ!BOX Eingabemaske](https://raw.githubusercontent.com/Q14siX/home-assistant-dyndns-manager/master/images/FRITZ!Box.png)

---

### 🔘 Home Assistant Features

- **Sensors** → show the current status and IP address
- **Buttons** → allow manual IP update
- **Service** → allows direct execution of a DynDNS update from automations or scripts

---

### 🛠 Development

1. Clone the repository:
   ```bash
   git clone https://github.com/Q14siX/home-assistant-dyndns-manager.git
   ```
2. Create a new provider file in `custom_components/dyndns_manager/provider/`.
3. Implement the update logic similar to other providers.

---

### 📬 Issues & Support

- **Report issues:** [GitHub Issues](https://github.com/Q14siX/home-assistant-dyndns-manager/issues)
- **Documentation:** [GitHub Readme](https://github.com/Q14siX/home-assistant-dyndns-manager)

---

### 📜 License

This project is licensed under the **MIT License** – see [LICENSE](LICENSE) for details.

---

💡 *DynDNS Manager – easy management of your dynamic DNS records directly in Home Assistant.*
   
