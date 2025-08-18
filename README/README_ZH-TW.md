# DynDNS Manager

[![版本](https://img.shields.io/github/v/release/Q14siX/home-assistant-dyndns-manager)](https://github.com/Q14siX/home-assistant-dyndns-manager/releases)  
[![MIT 授權](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
![語言](https://img.shields.io/badge/languages-20-blue.svg)  
![狀態](https://img.shields.io/badge/status-stable-brightgreen.svg)  
![下載](https://img.shields.io/github/downloads/Q14siX/home-assistant-dyndns-manager/total)

---

## 📌 Línguas / 语言 / 語言 / Jazyky / Sprog / Sprachen / Talen / Languages / Kielet / Langues / Nyelvek / Lingue / 言語 / Språk / Języki / Línguas / Языки / Idiomas / Språk / Diller

- 🇧🇷 [Português Brasileiro (pt-BR)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_PT-BR.md#portugues-brasileiro)
- 🇨🇳 [中文 (简体, zh-CN)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_ZH-CN.md#简体中文)
- 🇹🇼 [**中文 (繁體, zh-TW)**](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_ZH-TW.md#繁體中文)
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
- 🇸🇪 [Svenska (sv)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_SV.md#svenska)
- 🇹🇷 [Türkçe (tr)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_TR.md#türkçe)

---

## 繁體中文

[![Buy Me A Coffee](https://img.buymeacoffee.com/button-api/?text=Buy%20Stefan%20a%20tasty%20coffee&emoji=☕&slug=q14six&button_colour=FFDD00&font_colour=000000&font_family=Lato&outline_colour=000000&coffee_colour=ffffff)](https://buymeacoffee.com/q14six)

**DynDNS Manager** 是一個易於使用的 [Home Assistant](https://www.home-assistant.io/) 整合，允許您直接在 Home Assistant 中管理並更新您的 DynDNS 提供商。  
該整合目前支援以下提供商：

- **AllInkl**
- **Cloudflare**
- **DuckDNS**
- **NoIP**
- **Strato**

💡 此外，還可以設定 **Fritz!Box** 向 DynDNS Manager 發送更新。

功能包括：
- 自動更新 DynDNS 紀錄
- 透過 Home Assistant 介面的設定精靈 (Config Flow) 輕鬆配置
- 同時支援多個提供商
- 透過 Home Assistant 按鈕直接手動更新
- 透過 Home Assistant 服務直接執行 DynDNS 更新（適用於自動化和腳本）

---

### 🚀 安裝

#### 🔹 透過 HACS 安裝（推薦）

1. 在 Home Assistant 中開啟 **HACS**。
2. 前往 **整合**。
3. 點擊右上角的 **三個點**，選擇 **新增自訂倉庫**。
4. 新增以下倉庫：

   ```
   https://github.com/Q14siX/home-assistant-dyndns-manager
   ```

   分類：**Integration**

5. 在 HACS 中搜尋 **DynDNS Manager** 並安裝。
6. 重新啟動 Home Assistant。

---

#### 🔹 手動安裝

1. 從 [GitHub Releases](https://github.com/Q14siX/home-assistant-dyndns-manager/releases) 下載最新版本。
2. 解壓 ZIP 檔。
3. 將 `custom_components` 中的 **`dyndns_manager`** 資料夾複製到 Home Assistant 的 `custom_components` 資料夾：

   ```bash
   cp -r custom_components/dyndns_manager /config/custom_components/
   ```

4. 重新啟動 Home Assistant。

---

### ⚙️ 在 Home Assistant 中設定

1. 在 Home Assistant 中前往 **設定 → 裝置與服務**。
2. 點擊 **新增整合**。
3. 搜尋 **DynDNS Manager**。
4. 選擇所需的提供商 (DuckDNS, Strato, Cloudflare, NoIP, ALL-INKL)。
5. 輸入所需的帳號資訊 / API Key。
6. 完成！您的 DynDNS 紀錄將自動更新。

---

### 📄 設定

#### 支援的提供商與所需資料

| 提供商    | 所需資料 |
|-----------|----------|
| ALL-INKL  | 使用者名稱、密碼、網域 |
| Cloudflare| API Token, Zone ID, 網域 |
| DuckDNS   | API Token, 網域 |
| NoIP      | 使用者名稱、密碼、網域 |
| Strato    | 使用者名稱、密碼、網域 |

所有資料皆可透過 **Config Flow** 在 Home Assistant 介面中輸入，無需修改 `configuration.yaml`。

---

### 📡 Fritz!Box 整合

該整合也可以接收來自 Fritz!Box 的更新。

在 Fritz!Box 中，進入 **Internet → Freigaben → Dynamic DNS** 並輸入以下 URL：

```
http://<ha_host>:<ha_port>/dyndns-manager/?username=<username>&password=<pass>&ipv4=<ipaddr>&ipv6=<ip6addr>
```

- `<ha_host>` → 您的 Home Assistant 主機名稱或 IP 位址
- `<ha_port>` → Home Assistant 埠號 (預設: 8123)
- `<username>` / `<pass>` → 網頁存取帳號 (參見設定精靈)
- `<ipaddr>` / `<ip6addr>` → IPv4 和/或 IPv6 佔位符

💡 **提示:** 在 Fritz!Box 中僅需修改 `<ha_host>` 和 `<ha_port>`。其他值會在送出表單時由 Fritz!Box 自動替換。

![FRITZ!BOX 輸入介面](https://raw.githubusercontent.com/Q14siX/home-assistant-dyndns-manager/master/images/FRITZ!Box.png)

---

### 🔘 Home Assistant 功能

- **感測器** → 顯示目前狀態與 IP 位址
- **按鈕** → 手動更新 IP
- **服務** → 可從自動化或腳本直接執行 DynDNS 更新

---

### 🛠 開發

1. 複製倉庫：
   ```bash
   git clone https://github.com/Q14siX/home-assistant-dyndns-manager.git
   ```
2. 在 `custom_components/dyndns_manager/provider/` 資料夾中建立新的提供商檔案。
3. 依照現有提供商的範例實作更新邏輯。

---

### 📬 錯誤與支援

- **回報問題:** [GitHub Issues](https://github.com/Q14siX/home-assistant-dyndns-manager/issues)  
- **文件:** [GitHub Readme](https://github.com/Q14siX/home-assistant-dyndns-manager)

---

### 📜 授權

本專案使用 **MIT 授權** – 詳情請參閱 [LICENSE](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/LICENSE)。
