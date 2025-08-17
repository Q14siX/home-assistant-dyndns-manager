# DynDNS Manager

[![Versio](https://img.shields.io/github/v/release/Q14siX/home-assistant-dyndns-manager)](https://github.com/Q14siX/home-assistant-dyndns-manager/releases)  
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
![Kielet](https://img.shields.io/badge/languages-20-blue.svg)  
![Tila](https://img.shields.io/badge/status-stable-brightgreen.svg)  
![Lataukset](https://img.shields.io/github/downloads/Q14siX/home-assistant-dyndns-manager/total)

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
- [**Finnish (fi)**](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_FI.md#suomi)
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

## Suomi

**DynDNS Manager** on käyttäjäystävällinen integraatio [Home Assistant](https://www.home-assistant.io/):iin, jonka avulla voit hallita ja päivittää DynDNS-palveluntarjoajiasi suoraan Home Assistantista.  
Integraatio tukee tällä hetkellä seuraavia palveluntarjoajia:

- **AllInkl**
- **Cloudflare**
- **DuckDNS**
- **NoIP**
- **Strato**

💡 Lisäksi **Fritz!Box** voidaan määrittää lähettämään päivityksiä DynDNS Managerille.

Integraation ominaisuudet:
- DynDNS-tietueiden automaattinen päivitys
- Helppo konfigurointidialogi Home Assistant -käyttöliittymässä (Config Flow)
- Useiden palveluntarjoajien samanaikainen tuki
- Suora manuaalinen päivitys Home Assistant -painikkeiden kautta
- DynDNS-päivityksen suorittaminen suoraan Home Assistant -palvelun avulla (automaatiot ja skriptit)

---

### 🚀 Asennus

#### 🔹 Asennus HACS:n kautta (suositeltu)

1. Avaa **HACS** Home Assistantissasi.
2. Mene kohtaan **Integraatiot**.
3. Klikkaa **3 pistettä** oikeassa yläkulmassa ja valitse **Lisää mukautettu repository**.
4. Lisää seuraava repository:

   ```
   https://github.com/Q14siX/home-assistant-dyndns-manager
   ```

   Kategoria: **Integraatio**

5. Etsi nyt **DynDNS Manager** HACS:sta ja asenna se.
6. Käynnistä Home Assistant uudelleen.

---

#### 🔹 Manuaalinen asennus

1. Lataa uusin versio [GitHub Releases](https://github.com/Q14siX/home-assistant-dyndns-manager/releases) -sivulta.
2. Pura ZIP-tiedosto.
3. Kopioi kansio **`dyndns_manager`** `custom_components`-hakemistosta Home Assistantin `custom_components`-hakemistoon:

   ```bash
   cp -r custom_components/dyndns_manager /config/custom_components/
   ```

4. Käynnistä Home Assistant uudelleen.

---

### ⚙️ Määritys Home Assistantissa

1. Mene Home Assistantissa kohtaan **Asetukset → Laitteet & palvelut**.
2. Klikkaa **Lisää integraatio**.
3. Etsi **DynDNS Manager**.
4. Valitse haluamasi palveluntarjoaja (DuckDNS, Strato, Cloudflare, NoIP tai ALL-INKL).
5. Syötä tarvittavat kirjautumistiedot / API-avaimet.
6. Valmista! DynDNS-tietueesi päivittyvät nyt automaattisesti.

---

### 📄 Konfiguraatio

#### Tuetut palveluntarjoajat & tarvittavat tiedot

| Palveluntarjoaja | Tarvittavat tiedot |
|------------------|-------------------|
| ALL-INKL         | Käyttäjänimi, salasana, verkkotunnus |
| Cloudflare       | API-avain, Zone ID, verkkotunnus |
| DuckDNS          | API-avain, verkkotunnus |
| NoIP             | Käyttäjänimi, salasana, verkkotunnus |
| Strato           | Käyttäjänimi, salasana, verkkotunnus |

Kaikki tiedot syötetään helposti **Config Flow** -toiminnon kautta Home Assistantin käyttöliittymässä – `configuration.yaml`-muutoksia ei tarvita.

---

### 📡 Fritz!Box-yhteys

Integraatio voi vastaanottaa päivityksiä myös Fritz!Boxilta.

Fritz!Boxissa kohdassa **Internet → Jako → Dynamic DNS** syötä seuraava URL:

```
http://<ha_host>:<ha_port>/dyndns-manager/?username=<username>&password=<pass>&ipv4=<ipaddr>&ipv6=<ip6addr>
```

- `<ha_host>` → Home Assistantisi isäntänimi tai IP-osoite
- `<ha_port>` → Home Assistantin portti (oletus: 8123)
- `<username>` / `<pass>` → kirjautumistiedot verkkokäyttöön (katso määritysopas)
- `<ipaddr>` / `<ip6addr>` → paikkamerkit IPv4:lle ja/tai IPv6:lle

💡 **Huom:** Fritz!Boxissa tarvitsee muuttaa vain `<ha_host>` ja `<ha_port>`. Kaikki muut arvot (`<username>`, `<pass>`, `<ipaddr>`, `<ip6addr>`) korvataan automaattisesti Fritz!Boxin toimesta, kun täytät lomakkeen.

![FRITZ!BOX syöttölomake](https://raw.githubusercontent.com/Q14siX/home-assistant-dyndns-manager/master/images/FRITZ!Box.png)

---

### 🔘 Toiminnot Home Assistantissa

- **Sensorit** → näyttävät nykyisen tilan ja IP-osoitteen
- **Painikkeet** → mahdollistavat manuaalisen IP-päivityksen
- **Palvelu** → mahdollistaa DynDNS-päivityksen suorittamisen suoraan automaatioista tai skripteistä

---

### 🛠 Kehitys

1. Kloonaa repository:
   ```bash
   git clone https://github.com/Q14siX/home-assistant-dyndns-manager.git
   ```
2. Luo uusi palveluntarjoajatiedosto kansioon `custom_components/dyndns_manager/provider/`.
3. Toteuta päivityslogiikka muiden palveluntarjoajien mukaisesti.

---

### 📬 Virheet & tuki

- **Ilmoita ongelmista:** [GitHub Issues](https://github.com/Q14siX/home-assistant-dyndns-manager/issues)  
- **Dokumentaatio:** [GitHub Readme](https://github.com/Q14siX/home-assistant-dyndns-manager)

---

### 📜 Lisenssi

Tämä projekti on lisensoitu **MIT-lisenssillä** – katso [LICENSE](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/LICENSE) saadaksesi lisätietoja.
