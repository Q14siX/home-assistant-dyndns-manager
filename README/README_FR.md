# DynDNS Manager

[![Version](https://img.shields.io/github/v/release/Q14siX/home-assistant-dyndns-manager)](https://github.com/Q14siX/home-assistant-dyndns-manager/releases)  
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
![Langues](https://img.shields.io/badge/languages-20-blue.svg)  
![Statut](https://img.shields.io/badge/status-stable-brightgreen.svg)  
![Téléchargements](https://img.shields.io/github/downloads/Q14siX/home-assistant-dyndns-manager/total)

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
- [**French (fr)**](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_FR.md#français)
- [Hungarian (hu)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_HU.md#magyar)
- [Italian (it)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_IT.md#italiano)
- [Japanese (ja)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_JA.md#日本語)
- [Norwegian (Bokmål, nb)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_NB.md#norsk)
- [Polish (pl)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_PL.md#polski)
- [Portuguese (pt)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_PT.md#português)
- [Russian (ru)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_RU.md#Русский)
- [Spanish (es)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_ES.md#español)
- [Swedish (sv)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_SV.md#svenska)
- [Turkish (tr)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_TR.md#türkçe)

---

## Français

[![Buy Me A Coffee](https://img.buymeacoffee.com/button-api/?text=Buy%20Stefan%20a%20tasty%20coffee&emoji=☕&slug=q14six&button_colour=FFDD00&font_colour=000000&font_family=Lato&outline_colour=000000&coffee_colour=ffffff)](https://buymeacoffee.com/q14six)

**DynDNS Manager** est une intégration conviviale pour [Home Assistant](https://www.home-assistant.io/) qui vous permet de gérer et de mettre à jour vos fournisseurs DynDNS directement depuis Home Assistant.  
L’intégration prend actuellement en charge les fournisseurs suivants :

- **AllInkl**
- **Cloudflare**
- **DuckDNS**
- **NoIP**
- **Strato**

💡 De plus, une **Fritz!Box** peut être configurée pour envoyer des mises à jour au DynDNS Manager.

L’intégration offre :
- Mise à jour automatique de vos enregistrements DynDNS
- Dialogue de configuration simple via l’interface Home Assistant (Config Flow)
- Prise en charge de plusieurs fournisseurs simultanément
- Mise à jour manuelle directe via les boutons Home Assistant
- Exécution directe d’une mise à jour DynDNS via le service Home Assistant (pour automatisations et scripts)

---

### 🚀 Installation

#### 🔹 Installation via HACS (recommandé)

1. Ouvrez **HACS** dans votre Home Assistant.
2. Allez dans **Intégrations**.
3. Cliquez sur les **3 points** en haut à droite et sélectionnez **Ajouter un dépôt personnalisé**.
4. Ajoutez le dépôt suivant :

   ```
   https://github.com/Q14siX/home-assistant-dyndns-manager
   ```

   Catégorie : **Intégration**

5. Recherchez maintenant **DynDNS Manager** dans HACS et installez-le.
6. Redémarrez Home Assistant.

---

#### 🔹 Installation manuelle

1. Téléchargez la dernière version depuis [GitHub Releases](https://github.com/Q14siX/home-assistant-dyndns-manager/releases).
2. Décompressez le fichier ZIP.
3. Copiez le dossier **`dyndns_manager`** depuis `custom_components` vers le dossier `custom_components` de votre Home Assistant :

   ```bash
   cp -r custom_components/dyndns_manager /config/custom_components/
   ```

4. Redémarrez Home Assistant.

---

### ⚙️ Configuration dans Home Assistant

1. Dans Home Assistant, allez dans **Paramètres → Appareils & services**.
2. Cliquez sur **Ajouter une intégration**.
3. Recherchez **DynDNS Manager**.
4. Sélectionnez le fournisseur souhaité (DuckDNS, Strato, Cloudflare, NoIP ou ALL-INKL).
5. Entrez les identifiants / clés API requis.
6. Terminé ! Vos enregistrements DynDNS seront désormais mis à jour automatiquement.

---

### 📄 Configuration

#### Fournisseurs pris en charge & données requises

| Fournisseur  | Données requises |
|--------------|------------------|
| ALL-INKL     | Nom d’utilisateur, mot de passe, domaine |
| Cloudflare   | Jeton API, Zone ID, domaine |
| DuckDNS      | Jeton API, domaine |
| NoIP         | Nom d’utilisateur, mot de passe, domaine |
| Strato       | Nom d’utilisateur, mot de passe, domaine |

Toutes les données sont saisies facilement via le **Config Flow** dans l’interface Home Assistant – aucune modification de `configuration.yaml` nécessaire.

---

### 📡 Connexion Fritz!Box

L’intégration peut également recevoir des mises à jour d’une Fritz!Box.

Dans Fritz!Box sous **Internet → Partages → Dynamic DNS**, saisissez l’URL suivante :

```
http://<ha_host>:<ha_port>/dyndns-manager/?username=<username>&password=<pass>&ipv4=<ipaddr>&ipv6=<ip6addr>
```

- `<ha_host>` → Nom d’hôte ou adresse IP de votre Home Assistant
- `<ha_port>` → Port de Home Assistant (par défaut : 8123)
- `<username>` / `<pass>` → Identifiants d’accès Web (voir l’assistant de configuration)
- `<ipaddr>` / `<ip6addr>` → Variables pour IPv4 et/ou IPv6

💡 **Remarque :** Dans Fritz!Box, il suffit de modifier `<ha_host>` et `<ha_port>`. Toutes les autres valeurs (`<username>`, `<pass>`, `<ipaddr>`, `<ip6addr>`) sont automatiquement remplacées par Fritz!Box lorsque vous remplissez le formulaire.

![FRITZ!BOX formulaire](https://raw.githubusercontent.com/Q14siX/home-assistant-dyndns-manager/master/images/FRITZ!Box.png)

---

### 🔘 Fonctionnalités dans Home Assistant

- **Capteurs** → affichent l’état actuel et l’adresse IP
- **Boutons** → permettent une mise à jour manuelle de l’IP
- **Service** → permet d’exécuter directement une mise à jour DynDNS depuis les automatisations ou scripts

---

### 🛠 Développement

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/Q14siX/home-assistant-dyndns-manager.git
   ```
2. Créez un nouveau fichier fournisseur dans le dossier `custom_components/dyndns_manager/provider/`.
3. Implémentez la logique de mise à jour en vous basant sur les autres fournisseurs.

---

### 📬 Problèmes & support

- **Signaler un problème :** [GitHub Issues](https://github.com/Q14siX/home-assistant-dyndns-manager/issues)  
- **Documentation :** [GitHub Readme](https://github.com/Q14siX/home-assistant-dyndns-manager)

---

### 📜 Licence

Ce projet est sous licence **MIT** – voir [LICENSE](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/LICENSE) pour plus de détails.
