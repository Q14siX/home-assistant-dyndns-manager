# 📑 Changelog

Alle nennenswerten Änderungen dieses Projekts werden hier dokumentiert.  
All notable changes to this project will be documented in this file.

---

## 📦 Update auf v20250818.1615

### Fehlerbehebungen
- Behebung eines Problems, bei dem die Fritz!Box nach einer erfolgreichen DynDNS-Aktualisierung den Fehler meldete:  
  *„DynDNS-Fehler: Die DynDNS-Aktualisierung war erfolgreich, anschließend trat jedoch ein Fehler bei der DNS-Auflösung auf.“*

---

## 📦 Update to v20250818.1615

### Bug Fixes
- Fixed an issue where Fritz!Box reported an error after a successful DynDNS update:  
  *“DynDNS error: The DynDNS update was successful, but then an error occurred during DNS resolution.”*

---

## 📦 Update auf v20250815.1900

### Übersetzungen
- **Neu hinzugefügt (18 Sprachen):**
  - Brasilianisches Portugiesisch (pt-BR)
  - Chinesisch (Traditionell, zh-TW)
  - Chinesisch (Vereinfacht, zh-CN)
  - Dänisch (da)
  - Finnisch (fi)
  - Französisch (fr)
  - Italienisch (it)
  - Japanisch (ja)
  - Niederländisch (nl)
  - Norwegisch (Bokmål, nb)
  - Polnisch (pl)
  - Portugiesisch (pt)
  - Russisch (ru)
  - Schwedisch (sv)
  - Spanisch (es)
  - Tschechisch (cs)
  - Türkisch (tr)
  - Ungarisch (hu)
- **Aktualisiert:**
  - Deutsch (de)
  - Englisch (en)

---

## 📦 Update to v20250815.1900

### Translations
- **Newly added (18 languages):**
  - Brazilian Portuguese (pt-BR)
  - Chinese (Traditional, zh-TW)
  - Chinese (Simplified, zh-CN)
  - Danish (da)
  - Finnish (fi)
  - French (fr)
  - Italian (it)
  - Japanese (ja)
  - Dutch (nl)
  - Norwegian (Bokmål, nb)
  - Polish (pl)
  - Portuguese (pt)
  - Russian (ru)
  - Swedish (sv)
  - Spanish (es)
  - Czech (cs)
  - Turkish (tr)
  - Hungarian (hu)
- **Updated:**
  - German (de)
  - English (en)

---

## 📦 Update auf v20250815.1500

### Die wichtigsten Änderungen
- **Neuer Home Assistant Service**: `dyndns_manager.call_update`  
  - Kann direkt in **Automationen/Skripten** verwendet werden.  
  - **Parameter** (alle optional): `ha_host`, `ha_port`, `web_username`, `web_password`, `ipv4`, `ipv6`, `timeout`.  
  - **Defaults automatisch**: Host/Port werden aus der aktuellen HA-URL übernommen; externe **IPv4/IPv6** werden automatisch ermittelt, wenn nicht angegeben.  
  - Wenn **genau eine** Konfiguration existiert, werden `web_username`/`web_password` automatisch übernommen.
- **Service-UI**  
  - Fehlerbehebung bei der Formularanzeige (Felder werden korrekt angezeigt).
- **Übersetzungen**  
  - Verfügbar in **2 Sprachen**: Deutsch (de) und Englisch (en).

---

## 📦 Update to v20250815.1500

### Key Changes
- **New Home Assistant Service**: `dyndns_manager.call_update`  
  - Can be used directly in **automations/scripts**.  
  - **Parameters** (all optional): `ha_host`, `ha_port`, `web_username`, `web_password`, `ipv4`, `ipv6`, `timeout`.  
  - **Automatic defaults**: Host/port are derived from the current HA URL; external **IPv4/IPv6** are detected automatically if not provided.  
  - If **exactly one** configuration entry exists, `web_username`/`web_password` are applied automatically.
- **Service UI**  
  - Fixed form display (fields are shown correctly).
- **Translations**  
  - Available in **2 languages**: German (de) and English (en).

---

## 📦 Update auf v20250814.1415

### Die wichtigsten Änderungen
- **Unbegrenzte Integrationen**: Es können nun beliebig viele Integrationen hinzugefügt werden.  
- **Wichtig für All-Inkl.com**:  
  - Dieser Anbieter verwendet für jede Domain eigene Zugangsdaten.  
  - Wenn mehrere Domains dort aktualisiert werden sollen, muss dieser Anbieter mehrfach als Integration hinzugefügt werden.  
  - Die Zugangsdaten für den Webzugriff (Seite 4 bei Ersteinrichtung; Seite 3 bei Konfiguration) sollten identisch sein. Dadurch können durch einen einzigen URL-Aufruf (z. B. von einer FRITZ!Box oder Synology DiskStation) alle Integrationen mit diesen Zugangsdaten aktualisiert werden.  
- **Andere Anbieter**: Hier können beliebig viele Domains innerhalb einer Integration hinzugefügt werden.  
- **Alphabetische Sortierung**: Bei einer erneuten Konfiguration werden die Domains alphabetisch angezeigt, um das Auffinden bei vielen Einträgen zu erleichtern.  

---

## 📦 Update to v20250814.1415

### Key Changes
- **Unlimited Integrations**: You can now add as many integrations as you like.  
- **Important for All-Inkl.com**:  
  - This provider uses separate credentials for each domain.  
  - If you want to update multiple domains, you must add this provider multiple times as separate integrations.  
  - The web access credentials (page 4 during initial setup; page 3 during configuration) should be the same. This allows a single URL call (e.g., from a FRITZ!Box or Synology DiskStation) to update all integrations with those credentials.  
- **Other Providers**: You can add any number of domains within a single integration.  
- **Alphabetical Sorting**: When reconfiguring, domains are displayed in alphabetical order to make it easier to find the desired entry when many are added.
