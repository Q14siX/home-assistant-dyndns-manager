# DynDNS Manager

[![Verzió](https://img.shields.io/github/v/release/Q14siX/home-assistant-dyndns-manager)](https://github.com/Q14siX/home-assistant-dyndns-manager/releases)  
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
![Nyelvek](https://img.shields.io/badge/languages-20-blue.svg)  
![Állapot](https://img.shields.io/badge/status-stable-brightgreen.svg)  
![Letöltések](https://img.shields.io/github/downloads/Q14siX/home-assistant-dyndns-manager/total)

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
- [**Hungarian (hu)**](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_HU.md#magyar)
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

## Magyar

**DynDNS Manager** egy felhasználóbarát integráció a [Home Assistant](https://www.home-assistant.io/) számára, amely lehetővé teszi, hogy közvetlenül a Home Assistantból kezeld és frissítsd a DynDNS szolgáltatóidat.  
Az integráció jelenleg a következő szolgáltatókat támogatja:

- **AllInkl**
- **Cloudflare**
- **DuckDNS**
- **NoIP**
- **Strato**

💡 Ezen felül a **Fritz!Box** is konfigurálható úgy, hogy frissítéseket küldjön a DynDNS Managernek.

Az integráció a következőket kínálja:
- DynDNS bejegyzéseid automatikus frissítése
- Egyszerű konfigurációs párbeszédablak a Home Assistant felületén (Config Flow)
- Több szolgáltató egyidejű támogatása
- Közvetlen kézi frissítés a Home Assistant gombjaival
- DynDNS-frissítés közvetlen indítása Home Assistant szolgáltatáson keresztül (automatizálásokhoz és szkriptekhez)

---

### 🚀 Telepítés

#### 🔹 Telepítés HACS-en keresztül (ajánlott)

1. Nyisd meg a **HACS**-ot a Home Assistantban.
2. Menj az **Integrációk** részhez.
3. Kattints a **3 pontra** jobb felső sarokban, és válaszd a **Egyéni repository hozzáadása** lehetőséget.
4. Add hozzá a következő repository-t:

   ```
   https://github.com/Q14siX/home-assistant-dyndns-manager
   ```

   Kategória: **Integráció**

5. Keresd meg a **DynDNS Manager**-t a HACS-ban, és telepítsd.
6. Indítsd újra a Home Assistantot.

---

#### 🔹 Kézi telepítés

1. Töltsd le a legújabb verziót a [GitHub Releases](https://github.com/Q14siX/home-assistant-dyndns-manager/releases) oldalról.
2. Csomagold ki a ZIP fájlt.
3. Másold a **`dyndns_manager`** mappát a `custom_components` könyvtárból a Home Assistant `custom_components` könyvtárába:

   ```bash
   cp -r custom_components/dyndns_manager /config/custom_components/
   ```

4. Indítsd újra a Home Assistantot.

---

### ⚙️ Beállítás a Home Assistantban

1. A Home Assistantban menj a **Beállítások → Eszközök és szolgáltatások** menüpontra.
2. Kattints az **Integráció hozzáadása** gombra.
3. Keresd meg a **DynDNS Manager**-t.
4. Válaszd ki a kívánt szolgáltatót (DuckDNS, Strato, Cloudflare, NoIP vagy ALL-INKL).
5. Add meg a szükséges hitelesítő adatokat / API-kulcsokat.
6. Kész! A DynDNS bejegyzéseid mostantól automatikusan frissülnek.

---

### 📄 Konfiguráció

#### Támogatott szolgáltatók & szükséges adatok

| Szolgáltató | Szükséges adatok |
|-------------|------------------|
| ALL-INKL    | Felhasználónév, jelszó, domain |
| Cloudflare  | API token, Zone ID, domain |
| DuckDNS     | API token, domain |
| NoIP        | Felhasználónév, jelszó, domain |
| Strato      | Felhasználónév, jelszó, domain |

Minden adat kényelmesen megadható a **Config Flow**-n keresztül a Home Assistant felületén – nincs szükség `configuration.yaml` módosításokra.

---

### 📡 Fritz!Box integráció

Az integráció frissítéseket is tud fogadni egy Fritz!Box-tól.

A Fritz!Box-ban az **Internet → Megosztások → Dynamic DNS** alatt add meg a következő URL-t:

```
http://<ha_host>:<ha_port>/dyndns-manager/?username=<username>&password=<pass>&ipv4=<ipaddr>&ipv6=<ip6addr>
```

- `<ha_host>` → a Home Assistant hosztneve vagy IP címe
- `<ha_port>` → a Home Assistant portja (alapértelmezett: 8123)
- `<username>` / `<pass>` → webes hozzáférési hitelesítő adatok (lásd beállítási segéd)
- `<ipaddr>` / `<ip6addr>` → helyőrzők az IPv4 és/vagy IPv6 címekhez

💡 **Megjegyzés:** A Fritz!Box-ban csak a `<ha_host>` és `<ha_port>` értékeket kell megváltoztatni. Az összes többi értéket (`<username>`, `<pass>`, `<ipaddr>`, `<ip6addr>`) a Fritz!Box automatikusan behelyettesíti az űrlap kitöltésekor.

![FRITZ!BOX űrlap](https://raw.githubusercontent.com/Q14siX/home-assistant-dyndns-manager/master/images/FRITZ!Box.png)

---

### 🔘 Funkciók a Home Assistantban

- **Szenzorok** → megjelenítik az aktuális állapotot és az IP-címet
- **Gombok** → lehetővé teszik az IP kézi frissítését
- **Szolgáltatás** → lehetővé teszi egy DynDNS frissítés közvetlen végrehajtását automatizálásokból vagy szkriptekből

---

### 🛠 Fejlesztés

1. Klónozd a repository-t:
   ```bash
   git clone https://github.com/Q14siX/home-assistant-dyndns-manager.git
   ```
2. Hozz létre egy új szolgáltatófájlt a `custom_components/dyndns_manager/provider/` mappában.
3. Valósítsd meg a frissítési logikát a többi szolgáltatóhoz hasonlóan.

---

### 📬 Hibák & támogatás

- **Hibák jelentése:** [GitHub Issues](https://github.com/Q14siX/home-assistant-dyndns-manager/issues)  
- **Dokumentáció:** [GitHub Readme](https://github.com/Q14siX/home-assistant-dyndns-manager)

---

### 📜 Licenc

Ez a projekt **MIT licenc** alatt áll – részletekért lásd: [LICENSE](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/LICENSE).
