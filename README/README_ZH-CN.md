# DynDNS Manager

[![版本](https://img.shields.io/github/v/release/Q14siX/home-assistant-dyndns-manager)](https://github.com/Q14siX/home-assistant-dyndns-manager/releases)  
[![MIT 许可证](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
![语言](https://img.shields.io/badge/languages-20-blue.svg)  
![状态](https://img.shields.io/badge/status-stable-brightgreen.svg)  
![下载](https://img.shields.io/github/downloads/Q14siX/home-assistant-dyndns-manager/total)

---

## 📌 Línguas / 语言 / 語言 / Jazyky / Sprog / Sprachen / Talen / Languages / Kielet / Langues / Nyelvek / Lingue / 言語 / Språk / Języki / Línguas / Языки / Idiomas / Språk / Diller

- 🇧🇷 [Português Brasileiro (pt-BR)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_PT-BR.md#portugues-brasileiro)
- 🇨🇳 [**中文 (简体, zh-CN)**](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_ZH-CN.md#简体中文)
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
- 🇸🇪 [Svenska (sv)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_SV.md#svenska)
- 🇹🇷 [Türkçe (tr)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_TR.md#türkçe)

---

## 简体中文

[![Buy Me A Coffee](https://img.buymeacoffee.com/button-api/?text=Buy%20Stefan%20a%20tasty%20coffee&emoji=☕&slug=q14six&button_colour=FFDD00&font_colour=000000&font_family=Lato&outline_colour=000000&coffee_colour=ffffff)](https://buymeacoffee.com/q14six)

**DynDNS Manager** 是一个用户友好的 [Home Assistant](https://www.home-assistant.io/) 集成，允许您直接在 Home Assistant 中管理和更新您的 DynDNS 提供商。  
该集成目前支持以下提供商：

- **AllInkl**
- **Cloudflare**
- **DuckDNS**
- **NoIP**
- **Strato**

💡 此外，还可以将 **Fritz!Box** 配置为向 DynDNS Manager 发送更新。

功能包括：
- 自动更新 DynDNS 记录
- 通过 Home Assistant 界面中的配置向导 (Config Flow) 简单配置
- 同时支持多个提供商
- 通过 Home Assistant 按钮直接手动更新
- 通过 Home Assistant 服务直接执行 DynDNS 更新（适用于自动化和脚本）

---

### 🚀 安装

#### 🔹 通过 HACS 安装（推荐）

1. 在 Home Assistant 中打开 **HACS**。
2. 转到 **集成**。
3. 点击右上角的 **三个点**，选择 **添加自定义仓库**。
4. 添加以下仓库：

   ```
   https://github.com/Q14siX/home-assistant-dyndns-manager
   ```

   分类：**Integration**

5. 在 HACS 中搜索 **DynDNS Manager** 并安装。
6. 重启 Home Assistant。

---

#### 🔹 手动安装

1. 从 [GitHub Releases](https://github.com/Q14siX/home-assistant-dyndns-manager/releases) 下载最新版本。
2. 解压 ZIP 文件。
3. 将 `custom_components` 中的 **`dyndns_manager`** 文件夹复制到 Home Assistant 的 `custom_components` 文件夹中：

   ```bash
   cp -r custom_components/dyndns_manager /config/custom_components/
   ```

4. 重启 Home Assistant。

---

### ⚙️ Home Assistant 设置

1. 在 Home Assistant 中，转到 **设置 → 设备与服务**。
2. 点击 **添加集成**。
3. 搜索 **DynDNS Manager**。
4. 选择所需的提供商 (DuckDNS, Strato, Cloudflare, NoIP, ALL-INKL)。
5. 输入所需的凭证 / API Key。
6. 完成！您的 DynDNS 记录将自动更新。

---

### 📄 配置

#### 支持的提供商与所需数据

| 提供商    | 所需数据 |
|-----------|----------|
| ALL-INKL  | 用户名、密码、域名 |
| Cloudflare| API Token, Zone ID, 域名 |
| DuckDNS   | API Token, 域名 |
| NoIP      | 用户名、密码、域名 |
| Strato    | 用户名、密码、域名 |

所有数据都可通过 **Config Flow** 在 Home Assistant 界面输入，无需修改 `configuration.yaml`。

---

### 📡 Fritz!Box 集成

该集成还可以从 Fritz!Box 接收更新。

在 Fritz!Box 中，进入 **Internet → Freigaben → Dynamic DNS** 并输入以下 URL：

```
http://<ha_host>:<ha_port>/dyndns-manager/?username=<username>&password=<pass>&ipv4=<ipaddr>&ipv6=<ip6addr>
```

- `<ha_host>` → 您的 Home Assistant 主机名或 IP 地址
- `<ha_port>` → Home Assistant 端口 (默认: 8123)
- `<username>` / `<pass>` → Web 访问凭证 (见安装向导)
- `<ipaddr>` / `<ip6addr>` → IPv4 和/或 IPv6 占位符

💡 **提示:** 在 Fritz!Box 中只需修改 `<ha_host>` 和 `<ha_port>`。其他值会在提交表单时由 Fritz!Box 自动替换。

![FRITZ!BOX 输入界面](https://raw.githubusercontent.com/Q14siX/home-assistant-dyndns-manager/master/images/FRITZ!Box.png)

---

### 🔘 Home Assistant 功能

- **传感器** → 显示当前状态和 IP 地址
- **按钮** → 手动更新 IP
- **服务** → 可从自动化或脚本直接执行 DynDNS 更新

---

### 🛠 开发

1. 克隆仓库：
   ```bash
   git clone https://github.com/Q14siX/home-assistant-dyndns-manager.git
   ```
2. 在 `custom_components/dyndns_manager/provider/` 文件夹中创建新的提供商文件。
3. 按照现有提供商实现更新逻辑。

---

### 📬 错误与支持

- **提交问题:** [GitHub Issues](https://github.com/Q14siX/home-assistant-dyndns-manager/issues)  
- **文档:** [GitHub Readme](https://github.com/Q14siX/home-assistant-dyndns-manager)

---

### 📜 许可证

本项目采用 **MIT 许可证** – 详情参见 [LICENSE](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/LICENSE)。
