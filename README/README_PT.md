# DynDNS Manager

[![Versão](https://img.shields.io/github/v/release/Q14siX/home-assistant-dyndns-manager)](https://github.com/Q14siX/home-assistant-dyndns-manager/releases)  
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
![Idiomas](https://img.shields.io/badge/languages-20-blue.svg)  
![Estado](https://img.shields.io/badge/status-stable-brightgreen.svg)  
![Transferências](https://img.shields.io/github/downloads/Q14siX/home-assistant-dyndns-manager/total)

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
- [Norwegian (Bokmål, nb)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_NB.md#norsk)
- [Polish (pl)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_PL.md#polski)
- [**Portuguese (pt)**](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_PT.md#português)
- [Russian (ru)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_RU.md#Русский)
- [Spanish (es)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_ES.md#español)
- [Swedish (sv)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_SV.md#svenska)
- [Turkish (tr)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_TR.md#türkçe)

---

## Português

[![Buy Me A Coffee](https://img.buymeacoffee.com/button-api/?text=Buy%20Stefan%20a%20tasty%20coffee&emoji=☕&slug=q14six&button_colour=FFDD00&font_colour=000000&font_family=Lato&outline_colour=000000&coffee_colour=ffffff)](https://buymeacoffee.com/q14six)

**DynDNS Manager** é uma integração fácil de utilizar para o [Home Assistant](https://www.home-assistant.io/) que permite gerir e atualizar os seus fornecedores DynDNS diretamente a partir do Home Assistant.  
Atualmente, a integração suporta os seguintes fornecedores:

- **AllInkl**
- **Cloudflare**
- **DuckDNS**
- **NoIP**
- **Strato**

💡 Adicionalmente, é possível configurar uma **Fritz!Box** para enviar atualizações para o DynDNS Manager.

A integração oferece:
- Atualização automática dos seus registos DynDNS
- Assistente de configuração simples através da interface do Home Assistant (Config Flow)
- Suporte para vários fornecedores em simultâneo
- Atualização manual direta através dos botões do Home Assistant
- Execução direta de uma atualização DynDNS através do serviço do Home Assistant (para automatizações e scripts)

---

### 🚀 Instalação

#### 🔹 Instalação via HACS (recomendado)

1. Abra o **HACS** no seu Home Assistant.
2. Vá a **Integrações**.
3. Clique nos **3 pontos** no canto superior direito e selecione **Adicionar repositório personalizado**.
4. Adicione o seguinte repositório:

   ```
   https://github.com/Q14siX/home-assistant-dyndns-manager
   ```

   Categoria: **Integração**

5. Procure por **DynDNS Manager** no HACS e instale.
6. Reinicie o Home Assistant.

---

#### 🔹 Instalação manual

1. Transfira a versão mais recente a partir de [GitHub Releases](https://github.com/Q14siX/home-assistant-dyndns-manager/releases).
2. Extraia o ficheiro ZIP.
3. Copie a pasta **`dyndns_manager`** de `custom_components` para a pasta `custom_components` do seu Home Assistant:

   ```bash
   cp -r custom_components/dyndns_manager /config/custom_components/
   ```

4. Reinicie o Home Assistant.

---

### ⚙️ Configuração no Home Assistant

1. No Home Assistant, vá a **Definições → Dispositivos e serviços**.
2. Clique em **Adicionar integração**.
3. Pesquise por **DynDNS Manager**.
4. Selecione o fornecedor pretendido (DuckDNS, Strato, Cloudflare, NoIP ou ALL-INKL).
5. Introduza as credenciais / chaves de API necessárias.
6. Concluído! Os seus registos DynDNS serão agora atualizados automaticamente.

---

### 📄 Configuração

#### Fornecedores suportados e dados necessários

| Fornecedor | Dados necessários |
|-----------|-------------------|
| ALL-INKL  | Nome de utilizador, palavra‑passe, domínio |
| Cloudflare| Token de API, Zone ID, domínio |
| DuckDNS   | Token de API, domínio |
| NoIP      | Nome de utilizador, palavra‑passe, domínio |
| Strato    | Nome de utilizador, palavra‑passe, domínio |

Todos os dados são introduzidos de forma simples através do **Config Flow** na interface do Home Assistant — não são necessárias alterações ao `configuration.yaml`.

---

### 📡 Ligação Fritz!Box

A integração também pode receber atualizações de uma Fritz!Box.

Na Fritz!Box, em **Internet → Partilhas → Dynamic DNS**, introduza o seguinte URL:

```
http://<ha_host>:<ha_port>/dyndns-manager/?username=<username>&password=<pass>&ipv4=<ipaddr>&ipv6=<ip6addr>
```

- `<ha_host>` → nome do host ou endereço IP do seu Home Assistant
- `<ha_port>` → porta do Home Assistant (predefinição: 8123)
- `<username>` / `<pass>` → credenciais de acesso Web (ver assistente de configuração)
- `<ipaddr>` / `<ip6addr>` → placeholders para IPv4 e/ou IPv6

💡 **Nota:** Na Fritz!Box, apenas é necessário alterar `<ha_host>` e `<ha_port>`. Todos os restantes valores (`<username>`, `<pass>`, `<ipaddr>`, `<ip6addr>`) são automaticamente preenchidos pela Fritz!Box quando completar o formulário.

![Formulário FRITZ!BOX](https://raw.githubusercontent.com/Q14siX/home-assistant-dyndns-manager/master/images/FRITZ!Box.png)

---

### 🔘 Funcionalidades no Home Assistant

- **Sensores** → apresentam o estado atual e o endereço IP
- **Botões** → permitem a atualização manual do IP
- **Serviço** → permite executar diretamente uma atualização DynDNS a partir de automatizações ou scripts

---

### 🛠 Desenvolvimento

1. Clone o repositório:
   ```bash
   git clone https://github.com/Q14siX/home-assistant-dyndns-manager.git
   ```
2. Crie um novo ficheiro de fornecedor em `custom_components/dyndns_manager/provider/`.
3. Implemente a lógica de atualização seguindo o exemplo dos outros fornecedores.

---

### 📬 Erros e suporte

- **Comunicar problemas:** [GitHub Issues](https://github.com/Q14siX/home-assistant-dyndns-manager/issues)  
- **Documentação:** [GitHub Readme](https://github.com/Q14siX/home-assistant-dyndns-manager)

---

### 📜 Licença

Este projeto é disponibilizado sob a **licença MIT** — consulte [LICENSE](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/LICENSE) para mais detalhes.
