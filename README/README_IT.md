# DynDNS Manager

[![Versione](https://img.shields.io/github/v/release/Q14siX/home-assistant-dyndns-manager)](https://github.com/Q14siX/home-assistant-dyndns-manager/releases)  
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
![Lingue](https://img.shields.io/badge/languages-20-blue.svg)  
![Stato](https://img.shields.io/badge/status-stable-brightgreen.svg)  
![Download](https://img.shields.io/github/downloads/Q14siX/home-assistant-dyndns-manager/total)

---

## 📌 Línguas / 语言 / 語言 / Jazyky / Sprog / Sprachen / Talen / Languages / Kielet / Langues / Nyelvek / Lingue / 言語 / Språk / Języki / Línguas / Языки / Idiomas / Språk / Diller

- 🇧🇷 [Português Brasileiro (pt-BR)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_PT-BR.md#portugues-brasileiro)
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
- 🇮🇹 [**Italiano (it)**](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_IT.md#italiano)
- 🇯🇵 [日本語 (ja)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_JA.md#日本語)
- 🇳🇴 [Norsk bokmål (nb)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_NB.md#norsk)
- 🇵🇱 [Polski (pl)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_PL.md#polski)
- 🇵🇹 [Português (pt)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_PT.md#português)
- 🇷🇺 [Русский (ru)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_RU.md#Русский)
- 🇪🇸 [Español (es)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_ES.md#español)
- 🇸🇪 [Svenska (sv)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_SV.md#svenska)
- 🇹🇷 [Türkçe (tr)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_TR.md#türkçe)

---

## Italiano

[![Buy Me A Coffee](https://img.buymeacoffee.com/button-api/?text=Buy%20Stefan%20a%20tasty%20coffee&emoji=☕&slug=q14six&button_colour=FFDD00&font_colour=000000&font_family=Lato&outline_colour=000000&coffee_colour=ffffff)](https://buymeacoffee.com/q14six)

**DynDNS Manager** è un’integrazione intuitiva per [Home Assistant](https://www.home-assistant.io/) che consente di gestire e aggiornare i provider DynDNS direttamente da Home Assistant.  
Attualmente l’integrazione supporta i seguenti provider:

- **AllInkl**
- **Cloudflare**
- **DuckDNS**
- **NoIP**
- **Strato**

💡 Inoltre, è possibile configurare **Fritz!Box** affinché invii aggiornamenti a DynDNS Manager.

L’integrazione offre:
- Aggiornamento automatico dei record DynDNS
- Semplice procedura guidata di configurazione tramite l’interfaccia di Home Assistant (Config Flow)
- Supporto simultaneo per più provider
- Aggiornamento manuale diretto tramite pulsanti in Home Assistant
- Esecuzione diretta di un aggiornamento DynDNS tramite il servizio di Home Assistant (per automazioni e script)

---

### 🚀 Installazione

#### 🔹 Installazione tramite HACS (consigliata)

1. Apri **HACS** nel tuo Home Assistant.
2. Vai su **Integrazioni**.
3. Clicca sui **3 puntini** in alto a destra e seleziona **Aggiungi repository personalizzato**.
4. Aggiungi il seguente repository:

   ```
   https://github.com/Q14siX/home-assistant-dyndns-manager
   ```

   Categoria: **Integrazione**

5. Cerca **DynDNS Manager** in HACS e installalo.
6. Riavvia Home Assistant.

---

#### 🔹 Installazione manuale

1. Scarica l’ultima versione da [GitHub Releases](https://github.com/Q14siX/home-assistant-dyndns-manager/releases).
2. Estrai il file ZIP.
3. Copia la cartella **`dyndns_manager`** da `custom_components` nella cartella `custom_components` del tuo Home Assistant:

   ```bash
   cp -r custom_components/dyndns_manager /config/custom_components/
   ```

4. Riavvia Home Assistant.

---

### ⚙️ Configurazione in Home Assistant

1. In Home Assistant vai su **Impostazioni → Dispositivi e servizi**.
2. Clicca su **Aggiungi integrazione**.
3. Cerca **DynDNS Manager**.
4. Seleziona il provider desiderato (DuckDNS, Strato, Cloudflare, NoIP o ALL-INKL).
5. Inserisci le credenziali / gli API key richiesti.
6. Fatto! I tuoi record DynDNS verranno ora aggiornati automaticamente.

---

### 📄 Configurazione

#### Provider supportati & dati richiesti

| Provider   | Dati richiesti |
|------------|----------------|
| ALL-INKL   | Nome utente, password, dominio |
| Cloudflare | API token, Zone ID, dominio |
| DuckDNS    | API token, dominio |
| NoIP       | Nome utente, password, dominio |
| Strato     | Nome utente, password, dominio |

Tutti i dati vengono inseriti comodamente tramite **Config Flow** nell’interfaccia di Home Assistant – nessuna modifica a `configuration.yaml` necessaria.

---

### 📡 Collegamento Fritz!Box

L’integrazione può ricevere aggiornamenti anche da un Fritz!Box.

In Fritz!Box, sotto **Internet → Condivisioni → Dynamic DNS**, inserisci il seguente URL:

```
http://<ha_host>:<ha_port>/dyndns-manager/?username=<username>&password=<pass>&ipv4=<ipaddr>&ipv6=<ip6addr>
```

- `<ha_host>` → Nome host o indirizzo IP del tuo Home Assistant
- `<ha_port>` → Porta di Home Assistant (predefinita: 8123)
- `<username>` / `<pass>` → credenziali per l’accesso Web (vedi procedura guidata)
- `<ipaddr>` / `<ip6addr>` → segnaposto per IPv4 e/o IPv6

💡 **Nota:** In Fritz!Box è sufficiente modificare `<ha_host>` e `<ha_port>`. Tutti gli altri valori (`<username>`, `<pass>`, `<ipaddr>`, `<ip6addr>`) vengono sostituiti automaticamente da Fritz!Box quando compili il modulo.

![Modulo di inserimento FRITZ!BOX](https://raw.githubusercontent.com/Q14siX/home-assistant-dyndns-manager/master/images/FRITZ!Box.png)

---

### 🔘 Funzioni in Home Assistant

- **Sensori** → mostrano lo stato attuale e l’indirizzo IP
- **Pulsanti** → consentono l’aggiornamento manuale dell’IP
- **Servizio** → consente di eseguire direttamente un aggiornamento DynDNS da automazioni o script

---

### 🛠 Sviluppo

1. Clona il repository:
   ```bash
   git clone https://github.com/Q14siX/home-assistant-dyndns-manager.git
   ```
2. Crea un nuovo file del provider nella cartella `custom_components/dyndns_manager/provider/`.
3. Implementa la logica di aggiornamento seguendo l’esempio degli altri provider.

---

### 📬 Problemi & supporto

- **Segnala un problema:** [GitHub Issues](https://github.com/Q14siX/home-assistant-dyndns-manager/issues)  
- **Documentazione:** [GitHub Readme](https://github.com/Q14siX/home-assistant-dyndns-manager)

---

### 📜 Licenza

Questo progetto è rilasciato sotto **licenza MIT** – vedi [LICENSE](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/LICENSE) per i dettagli.
