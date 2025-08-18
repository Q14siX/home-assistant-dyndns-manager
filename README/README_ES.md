# DynDNS Manager

[![Versión](https://img.shields.io/github/v/release/Q14siX/home-assistant-dyndns-manager)](https://github.com/Q14siX/home-assistant-dyndns-manager/releases)  
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
![Idiomas](https://img.shields.io/badge/languages-20-blue.svg)  
![Estado](https://img.shields.io/badge/status-stable-brightgreen.svg)  
![Descargas](https://img.shields.io/github/downloads/Q14siX/home-assistant-dyndns-manager/total)

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
- 🇵🇱 [Polski (pl)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_PL.md#polski)
- 🇵🇹 [Português (pt)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_PT.md#português)
- 🇷🇺 [Русский (ru)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_RU.md#Русский)
- 🇪🇸 [**Español (es)**](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_ES.md#español)
- 🇸🇪 [Svenska (sv)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_SV.md#svenska)
- 🇹🇷 [Türkçe (tr)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_TR.md#türkçe)

---

## Español

[![Buy Me A Coffee](https://img.buymeacoffee.com/button-api/?text=Buy%20Stefan%20a%20tasty%20coffee&emoji=☕&slug=q14six&button_colour=FFDD00&font_colour=000000&font_family=Lato&outline_colour=000000&coffee_colour=ffffff)](https://buymeacoffee.com/q14six)

**DynDNS Manager** es una integración fácil de usar para [Home Assistant](https://www.home-assistant.io/) que te permite gestionar y actualizar tus proveedores DynDNS directamente desde Home Assistant.  
La integración actualmente admite los siguientes proveedores:

- **AllInkl**
- **Cloudflare**
- **DuckDNS**
- **NoIP**
- **Strato**

💡 Además, se puede configurar una **Fritz!Box** para que envíe actualizaciones al DynDNS Manager.

La integración ofrece:
- Actualización automática de tus registros DynDNS
- Sencillo asistente de configuración a través de la interfaz de Home Assistant (Config Flow)
- Compatibilidad con varios proveedores simultáneamente
- Actualización manual directa mediante botones de Home Assistant
- Ejecución directa de una actualización DynDNS mediante el servicio de Home Assistant (para automatizaciones y scripts)

---

### 🚀 Instalación

#### 🔹 Instalación mediante HACS (recomendado)

1. Abre **HACS** en tu Home Assistant.
2. Ve a **Integrations / Integraciones**.
3. Haz clic en los **3 puntos** de la esquina superior derecha y selecciona **Add custom repository / Añadir repositorio personalizado**.
4. Añade el siguiente repositorio:

   ```
   https://github.com/Q14siX/home-assistant-dyndns-manager
   ```

   Categoría: **Integration / Integración**

5. Busca **DynDNS Manager** en HACS e instálalo.
6. Reinicia Home Assistant.

---

#### 🔹 Instalación manual

1. Descarga la última versión desde [GitHub Releases](https://github.com/Q14siX/home-assistant-dyndns-manager/releases).
2. Descomprime el archivo ZIP.
3. Copia la carpeta **`dyndns_manager`** de `custom_components` a la carpeta `custom_components` de tu Home Assistant:

   ```bash
   cp -r custom_components/dyndns_manager /config/custom_components/
   ```

4. Reinicia Home Assistant.

---

### ⚙️ Configuración en Home Assistant

1. En Home Assistant, ve a **Ajustes → Dispositivos y servicios**.
2. Haz clic en **Añadir integración**.
3. Busca **DynDNS Manager**.
4. Selecciona el proveedor deseado (DuckDNS, Strato, Cloudflare, NoIP o ALL-INKL).
5. Introduce las credenciales / claves API requeridas.
6. ¡Listo! Tus registros DynDNS se actualizarán automáticamente.

---

### 📄 Configuración

#### Proveedores compatibles y datos necesarios

| Proveedor  | Datos necesarios |
|------------|------------------|
| ALL-INKL   | Nombre de usuario, contraseña, dominio |
| Cloudflare | Token API, Zone ID, dominio |
| DuckDNS    | Token API, dominio |
| NoIP       | Nombre de usuario, contraseña, dominio |
| Strato     | Nombre de usuario, contraseña, dominio |

Todos los datos se introducen cómodamente mediante **Config Flow** en la interfaz de Home Assistant; no es necesario modificar `configuration.yaml`.

---

### 📡 Integración con Fritz!Box

La integración también puede recibir actualizaciones desde una Fritz!Box.

En Fritz!Box, en **Internet → Compartir / Freigaben → Dynamic DNS**, introduce la siguiente URL:

```
http://<ha_host>:<ha_port>/dyndns-manager/?username=<username>&password=<pass>&ipv4=<ipaddr>&ipv6=<ip6addr>
```

- `<ha_host>` → nombre de host o dirección IP de tu Home Assistant
- `<ha_port>` → puerto de Home Assistant (predeterminado: 8123)
- `<username>` / `<pass>` → credenciales de acceso web (consulta el asistente de configuración)
- `<ipaddr>` / `<ip6addr>` → marcadores de posición para IPv4 y/o IPv6

💡 **Nota:** En Fritz!Box solo necesitas cambiar `<ha_host>` y `<ha_port>`. Los demás valores (`<username>`, `<pass>`, `<ipaddr>`, `<ip6addr>`) se reemplazan automáticamente al completar el formulario.

![Formulario FRITZ!BOX](https://raw.githubusercontent.com/Q14siX/home-assistant-dyndns-manager/master/images/FRITZ!Box.png)

---

### 🔘 Funciones en Home Assistant

- **Sensores** → muestran el estado actual y la dirección IP
- **Botones** → permiten actualizar la IP manualmente
- **Servicio** → permite ejecutar directamente una actualización DynDNS desde automatizaciones o scripts

---

### 🛠 Desarrollo

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Q14siX/home-assistant-dyndns-manager.git
   ```
2. Crea un nuevo archivo de proveedor en la carpeta `custom_components/dyndns_manager/provider/`.
3. Implementa la lógica de actualización siguiendo el ejemplo de los demás proveedores.

---

### 📬 Errores y soporte

- **Informar incidencias:** [GitHub Issues](https://github.com/Q14siX/home-assistant-dyndns-manager/issues)  
- **Documentación:** [GitHub Readme](https://github.com/Q14siX/home-assistant-dyndns-manager)

---

### 📜 Licencia

Este proyecto está bajo la **licencia MIT**; consulta [LICENSE](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/LICENSE) para más detalles.
