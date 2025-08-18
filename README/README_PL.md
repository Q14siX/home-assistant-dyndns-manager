# DynDNS Manager

[![Wersja](https://img.shields.io/github/v/release/Q14siX/home-assistant-dyndns-manager)](https://github.com/Q14siX/home-assistant-dyndns-manager/releases)  
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
![Języki](https://img.shields.io/badge/languages-20-blue.svg)  
![Status](https://img.shields.io/badge/status-stable-brightgreen.svg)  
![Pobrania](https://img.shields.io/github/downloads/Q14siX/home-assistant-dyndns-manager/total)

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
- 🇮🇹 [Italiano (it)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_IT.md#italiano)
- 🇯🇵 [日本語 (ja)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_JA.md#日本語)
- 🇳🇴 [Norsk bokmål (nb)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_NB.md#norsk)
- 🇵🇱 [**Polski (pl)**](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_PL.md#polski)
- 🇵🇹 [Português (pt)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_PT.md#português)
- 🇷🇺 [Русский (ru)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_RU.md#Русский)
- 🇪🇸 [Español (es)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_ES.md#español)
- 🇸🇪 [Svenska (sv)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_SV.md#svenska)
- 🇹🇷 [Türkçe (tr)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_TR.md#türkçe)

---

## Polski

<a href="https://www.buymeacoffee.com/Q14siX" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

**DynDNS Manager** to przyjazna dla użytkownika integracja dla [Home Assistant](https://www.home-assistant.io/), która umożliwia zarządzanie i aktualizowanie dostawców DynDNS bezpośrednio z Home Assistant.  
Integracja obecnie obsługuje następujących dostawców:

- **AllInkl**
- **Cloudflare**
- **DuckDNS**
- **NoIP**
- **Strato**

> [!NOTE]
> Dodatkowo można skonfigurować **Fritz!Box**, aby wysyłał aktualizacje do DynDNS Managera.

Integracja oferuje:
- Automatyczną aktualizację wpisów DynDNS
- Prosty kreator konfiguracji w interfejsie Home Assistant (Config Flow)
- Obsługę wielu dostawców jednocześnie
- Bezpośrednią ręczną aktualizację za pomocą przycisków w Home Assistant
- Bezpośrednie wywołanie aktualizacji DynDNS poprzez usługę Home Assistant (do automatyzacji i skryptów)

---

### 🚀 Instalacja

#### 🔹 Instalacja przez HACS (zalecane)

1. Otwórz **HACS** w swoim Home Assistancie.
2. Przejdź do **Integrations / Integracje**.
3. Kliknij **3 kropki** w prawym górnym rogu i wybierz **Dodaj niestandardowe repozytorium**.
4. Dodaj następujące repozytorium:

   ```
   https://github.com/Q14siX/home-assistant-dyndns-manager
   ```

   Kategoria: **Integration / Integracja**

5. Wyszukaj **DynDNS Manager** w HACS i zainstaluj.
6. Uruchom ponownie Home Assistanta.

---

#### 🔹 Instalacja ręczna

1. Pobierz najnowszą wersję z [GitHub Releases](https://github.com/Q14siX/home-assistant-dyndns-manager/releases).
2. Rozpakuj plik ZIP.
3. Skopiuj folder **`dyndns_manager`** z `custom_components` do katalogu `custom_components` Twojego Home Assistanta:

   ```bash
   cp -r custom_components/dyndns_manager /config/custom_components/
   ```

4. Uruchom ponownie Home Assistanta.

---

### ⚙️ Konfiguracja w Home Assistant

1. W Home Assistant przejdź do **Ustawienia → Urządzenia i usługi**.
2. Kliknij **Dodaj integrację**.
3. Wyszukaj **DynDNS Manager**.
4. Wybierz żądanego dostawcę (DuckDNS, Strato, Cloudflare, NoIP lub ALL-INKL).
5. Wprowadź wymagane dane logowania / klucze API.
6. Gotowe! Wpisy DynDNS będą teraz aktualizowane automatycznie.

---

### 📄 Konfiguracja

#### Obsługiwani dostawcy i wymagane dane

| Dostawca   | Wymagane dane |
|------------|---------------|
| ALL-INKL   | Nazwa użytkownika, hasło, domena |
| Cloudflare | Token API, Zone ID, domena |
| DuckDNS    | Token API, domena |
| NoIP       | Nazwa użytkownika, hasło, domena |
| Strato     | Nazwa użytkownika, hasło, domena |

Wszystkie dane wprowadza się wygodnie przez **Config Flow** w interfejsie Home Assistant — bez potrzeby modyfikacji `configuration.yaml`.

---

### 📡 Integracja z Fritz!Box

Integracja może również odbierać aktualizacje z Fritz!Boxa.

W Fritz!Box w **Internet → Udostępnianie → Dynamic DNS** wprowadź następujący adres URL:

```
http://<ha_host>:<ha_port>/dyndns-manager/?username=<username>&password=<pass>&ipv4=<ipaddr>&ipv6=<ip6addr>
```

- `<ha_host>` → nazwa hosta lub adres IP Twojego Home Assistanta
- `<ha_port>` → port Home Assistanta (domyślnie: 8123)
- `<username>` / `<pass>` → dane logowania do dostępu przez WWW (patrz kreator konfiguracji)
- `<ipaddr>` / `<ip6addr>` → symbole zastępcze dla adresów IPv4 i/lub IPv6

> [!TIP]
> W Fritz!Box wystarczy zmienić tylko `<ha_host>` i `<ha_port>`. Pozostałe wartości (`<username>`, `<pass>`, `<ipaddr>`, `<ip6addr>`) zostaną automatycznie podstawione przez Fritz!Box po wypełnieniu formularza.

![Formularz FRITZ!BOX](https://raw.githubusercontent.com/Q14siX/home-assistant-dyndns-manager/master/images/FRITZ!Box.png)

---

### 🔘 Funkcje w Home Assistant

- **Sensory** → pokazują bieżący stan i adres IP
- **Przyciski** → umożliwiają ręczną aktualizację IP
- **Usługa** → umożliwia bezpośrednie wykonanie aktualizacji DynDNS z automatyzacji lub skryptów

---

### 🛠 Rozwój

1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/Q14siX/home-assistant-dyndns-manager.git
   ```
2. Utwórz nowy plik dostawcy w katalogu `custom_components/dyndns_manager/provider/`.
3. Zaimplementuj logikę aktualizacji zgodnie z innymi dostawcami.

---

### 📬 Błędy i wsparcie

- **Zgłaszanie problemów:** [GitHub Issues](https://github.com/Q14siX/home-assistant-dyndns-manager/issues)  
- **Dokumentacja:** [GitHub Readme](https://github.com/Q14siX/home-assistant-dyndns-manager)

---

### 📜 Licencja

Ten projekt jest objęty licencją **MIT** — szczegóły w pliku [LICENSE](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/LICENSE).
