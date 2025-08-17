# DynDNS Manager

[![Version](https://img.shields.io/github/v/release/Q14siX/home-assistant-dyndns-manager)](https://github.com/Q14siX/home-assistant-dyndns-manager/releases)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Languages](https://img.shields.io/badge/languages-20-blue.svg)
![Status](https://img.shields.io/badge/status-stable-brightgreen.svg)
![Downloads](https://img.shields.io/github/downloads/Q14siX/home-assistant-dyndns-manager/total)

---

## 📌 Línguas / 语言 / 語言 / Jazyky / Sprog / Sprachen / Talen / Languages / Kielet / Langues / Nyelvek / Lingue / 言語 / Språk / Języki / Línguas / Языки / Idiomas / Språk / Diller
- [Brazilian Portuguese (pt-BR)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_PT-BR.md#portugues-brasileiro)
- [Chinese (Simplified, zh-CN)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_ZH-CN.md#简体中文)
- [Chinese (Traditional, zh-TW)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_ZH-TW.md#繁體中文)
- [Czech (cs)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_CS.md#czech)
- [Danish (da)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_DA.md#dansk)
- [Deutsch (de)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_DE.md#deutsch)
- [Dutch (nl)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_NL.md#dutch)
- [**English (en)**](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_EN.md#english)
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

This project is licensed under the **MIT License** – see [LICENSE](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/LICENSE) for details.

---

💡 *DynDNS Manager – easy management of your dynamic DNS records directly in Home Assistant.*
   
