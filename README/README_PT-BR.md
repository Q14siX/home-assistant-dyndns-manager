# Gerenciador DynDNS

[![Versão](https://img.shields.io/github/v/release/Q14siX/home-assistant-dyndns-manager)](https://github.com/Q14siX/home-assistant-dyndns-manager/releases)
[![Licença MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Idiomas](https://img.shields.io/badge/languages-20-blue.svg)
![Status](https://img.shields.io/badge/status-stable-brightgreen.svg)
![Downloads](https://img.shields.io/github/downloads/Q14siX/home-assistant-dyndns-manager/total)

---

## 📌 Línguas / 语言 / 語言 / Jazyky / Sprog / Sprachen / Talen / Languages / Kielet / Langues / Nyelvek / Lingue / 言語 / Språk / Języki / Línguas / Языки / Idiomas / Språk / Diller

- 🇧🇷 [**Português Brasileiro (pt-BR)**](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_PT-BR.md#portugues-brasileiro)
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
- 🇸🇪 [Svenska (sv)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_SV.md#svenska)
- 🇹🇷 [Türkçe (tr)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_TR.md#türkçe)

---

## Portugues Brasileiro

[![Buy Me A Coffee](https://img.buymeacoffee.com/button-api/?text=Buy%20Stefan%20a%20tasty%20coffee&emoji=☕&slug=q14six&button_colour=FFDD00&font_colour=000000&font_family=Lato&outline_colour=000000&coffee_colour=ffffff)](https://buymeacoffee.com/q14six)

**DynDNS Manager** é uma integração amigável do [Home Assistant](https://www.home-assistant.io/) que permite gerenciar e atualizar seus provedores DynDNS diretamente a partir do Home Assistant.  
Atualmente, a integração suporta os seguintes provedores:

- **AllInkl**
- **Cloudflare**
- **DuckDNS**
- **NoIP**
- **Strato**

💡 Além disso, um **Fritz!Box** pode ser configurado para enviar uma atualização para o DynDNS Manager.

A integração oferece:
- Atualização automática de seus registros DynDNS
- Diálogo de configuração simples pela interface do Home Assistant (Config Flow)
- Suporte a múltiplos provedores simultaneamente
- Atualização manual direta através de botões no Home Assistant
- Execução direta de uma atualização DynDNS via serviço do Home Assistant (para automações e scripts)

---

### 🚀 Instalação

#### 🔹 Instalação via HACS (recomendada)

1. Abra o **HACS** no seu Home Assistant.
2. Vá para **Integrações**.
3. Clique nos **3 pontos** no canto superior direito e selecione **Adicionar repositório personalizado**.
4. Adicione o seguinte repositório:

   ```
   https://github.com/Q14siX/home-assistant-dyndns-manager
   ```

   Categoria: **Integração**

5. Procure por **DynDNS Manager** no HACS e instale-o.
6. Reinicie o Home Assistant.

---

#### 🔹 Instalação manual

1. Baixe a versão mais recente em [GitHub Releases](https://github.com/Q14siX/home-assistant-dyndns-manager/releases).
2. Extraia o arquivo ZIP.
3. Copie a pasta **`dyndns_manager`** de `custom_components` para a pasta `custom_components` do seu Home Assistant:

   ```bash
   cp -r custom_components/dyndns_manager /config/custom_components/
   ```

4. Reinicie o Home Assistant.

---

### ⚙️ Configuração no Home Assistant

1. No Home Assistant, vá para **Configurações → Dispositivos e Serviços**.
2. Clique em **Adicionar integração**.
3. Procure por **DynDNS Manager**.
4. Selecione o provedor desejado (DuckDNS, Strato, Cloudflare, NoIP ou ALL-INKL).
5. Insira as credenciais / chaves de API necessárias.
6. Pronto! Seus registros DynDNS agora serão atualizados automaticamente.

---

### 📄 Configuração

#### Provedores suportados & dados necessários

| Provedor    | Dados necessários |
|-------------|------------------|
| ALL-INKL    | Nome de usuário, Senha, Domínio |
| Cloudflare  | Token de API, Zone ID, Domínio |
| DuckDNS     | Token de API, Domínio |
| NoIP        | Nome de usuário, Senha, Domínio |
| Strato      | Nome de usuário, Senha, Domínio |

Todos os dados são inseridos facilmente via **Config Flow** na interface do Home Assistant – não é necessário alterar o `configuration.yaml`.

---

### 📡 Integração com Fritz!Box

A integração também pode receber atualizações de um Fritz!Box.

Na Fritz!Box, em **Internet → Compartilhamentos → Dynamic DNS**, insira a seguinte URL:

```
http://<ha_host>:<ha_port>/dyndns-manager/?username=<username>&password=<pass>&ipv4=<ipaddr>&ipv6=<ip6addr>
```

- `<ha_host>` → Nome do host ou endereço IP do seu Home Assistant
- `<ha_port>` → Porta do Home Assistant (padrão: 8123)
- `<username>` / `<pass>` → Credenciais de acesso à Web (veja o assistente de configuração)
- `<ipaddr>` / `<ip6addr>` → Espaços reservados para IPv4 e/ou IPv6

💡 **Nota:** Na Fritz!Box, apenas `<ha_host>` e `<ha_port>` precisam ser ajustados na URL. Todos os outros valores (`<username>`, `<pass>`, `<ipaddr>`, `<ip6addr>`) serão substituídos automaticamente pela Fritz!Box ao preencher o formulário.

![Tela Fritz!Box](https://raw.githubusercontent.com/Q14siX/home-assistant-dyndns-manager/master/images/FRITZ!Box.png)

---

### 🔘 Funções no Home Assistant

- **Sensores** → mostram o status atual e o endereço IP
- **Botões** → permitem atualização manual do IP
- **Serviço** → executa diretamente uma atualização DynDNS a partir de automações ou scripts

---

### 🛠 Desenvolvimento

1. Clone o repositório:
   ```bash
   git clone https://github.com/Q14siX/home-assistant-dyndns-manager.git
   ```
2. Crie um novo arquivo de provedor na pasta `custom_components/dyndns_manager/provider/`.
3. Implemente a lógica de atualização conforme os outros provedores.

---

### 📬 Problemas & Suporte

- **Reportar problemas:** [GitHub Issues](https://github.com/Q14siX/home-assistant-dyndns-manager/issues)
- **Documentação:** [GitHub Readme](https://github.com/Q14siX/home-assistant-dyndns-manager)

---

### 📜 Licença

Este projeto está sob a **Licença MIT** – veja [LICENSE](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/LICENSE) para mais detalhes.
