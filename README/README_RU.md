# DynDNS Manager

[![Версия](https://img.shields.io/github/v/release/Q14siX/home-assistant-dyndns-manager)](https://github.com/Q14siX/home-assistant-dyndns-manager/releases)  
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
![Языки](https://img.shields.io/badge/languages-20-blue.svg)  
![Статус](https://img.shields.io/badge/status-stable-brightgreen.svg)  
![Загрузки](https://img.shields.io/github/downloads/Q14siX/home-assistant-dyndns-manager/total)

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
- [Portuguese (pt)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_PT.md#português)
- [**Russian (ru)**](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_RU.md#Русский)
- [Spanish (es)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_ES.md#español)
- [Swedish (sv)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_SV.md#svenska)
- [Turkish (tr)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_TR.md#türkçe)

---

## Русский

[![Buy Me A Coffee](https://img.buymeacoffee.com/button-api/?text=Buy%20Stefan%20a%20tasty%20coffee&emoji=☕&slug=q14six&button_colour=FFDD00&font_colour=000000&font_family=Lato&outline_colour=000000&coffee_colour=ffffff)](https://buymeacoffee.com/q14six)

**DynDNS Manager** — это удобная интеграция для [Home Assistant](https://www.home-assistant.io/), которая позволяет управлять провайдерами DynDNS и обновлять их напрямую из Home Assistant.  
На данный момент интеграция поддерживает следующих провайдеров:

- **AllInkl**
- **Cloudflare**
- **DuckDNS**
- **NoIP**
- **Strato**

💡 Кроме того, можно настроить **Fritz!Box** так, чтобы он отправлял обновления в DynDNS Manager.

Интеграция предлагает:
- Автоматическое обновление записей DynDNS
- Простой мастер настройки через интерфейс Home Assistant (Config Flow)
- Поддержку нескольких провайдеров одновременно
- Прямое ручное обновление через кнопки Home Assistant
- Прямой запуск обновления DynDNS через сервис Home Assistant (для автоматизаций и скриптов)

---

### 🚀 Установка

#### 🔹 Установка через HACS (рекомендуется)

1. Откройте **HACS** в Home Assistant.
2. Перейдите в раздел **Integrations / Интеграции**.
3. Нажмите **3 точки** в правом верхнем углу и выберите **Добавить пользовательский репозиторий**.
4. Добавьте следующий репозиторий:

   ```
   https://github.com/Q14siX/home-assistant-dyndns-manager
   ```

   Категория: **Integration / Интеграция**

5. Найдите **DynDNS Manager** в HACS и установите.
6. Перезапустите Home Assistant.

---

#### 🔹 Ручная установка

1. Скачайте последнюю версию с [GitHub Releases](https://github.com/Q14siX/home-assistant-dyndns-manager/releases).
2. Распакуйте ZIP‑файл.
3. Скопируйте папку **`dyndns_manager`** из `custom_components` в папку `custom_components` вашего Home Assistant:

   ```bash
   cp -r custom_components/dyndns_manager /config/custom_components/
   ```

4. Перезапустите Home Assistant.

---

### ⚙️ Настройка в Home Assistant

1. В Home Assistant перейдите в **Настройки → Устройства и службы**.
2. Нажмите **Добавить интеграцию**.
3. Найдите **DynDNS Manager**.
4. Выберите нужного провайдера (DuckDNS, Strato, Cloudflare, NoIP или ALL-INKL).
5. Введите необходимые учетные данные / API‑ключи.
6. Готово! Записи DynDNS теперь будут обновляться автоматически.

---

### 📄 Конфигурация

#### Поддерживаемые провайдеры и необходимые данные

| Провайдер   | Необходимые данные |
|------------|--------------------|
| ALL-INKL   | Имя пользователя, пароль, домен |
| Cloudflare | API‑токен, Zone ID, домен |
| DuckDNS    | API‑токен, домен |
| NoIP       | Имя пользователя, пароль, домен |
| Strato     | Имя пользователя, пароль, домен |

Ввод всех данных выполняется удобно через **Config Flow** в интерфейсе Home Assistant — нет необходимости менять `configuration.yaml`.

---

### 📡 Интеграция с Fritz!Box

Интеграция может получать обновления и от Fritz!Box.

В Fritz!Box в разделе **Internet → Freigaben / Общий доступ → Dynamic DNS** укажите следующий URL:

```
http://<ha_host>:<ha_port>/dyndns-manager/?username=<username>&password=<pass>&ipv4=<ipaddr>&ipv6=<ip6addr>
```

- `<ha_host>` → имя хоста или IP‑адрес вашего Home Assistant
- `<ha_port>` → порт Home Assistant (по умолчанию: 8123)
- `<username>` / `<pass>` → учетные данные для веб‑доступа (см. мастер настройки)
- `<ipaddr>` / `<ip6addr>` → плейсхолдеры для IPv4 и/или IPv6

💡 **Примечание:** В Fritz!Box достаточно изменить только `<ha_host>` и `<ha_port>`. Остальные значения (`<username>`, `<pass>`, `<ipaddr>`, `<ip6addr>`) Fritz!Box подставит автоматически при заполнении формы.

![Форма FRITZ!BOX](https://raw.githubusercontent.com/Q14siX/home-assistant-dyndns-manager/master/images/FRITZ!Box.png)

---

### 🔘 Функции в Home Assistant

- **Датчики** → отображают текущий статус и IP‑адрес
- **Кнопки** → позволяют вручную обновлять IP
- **Сервис** → позволяет напрямую запускать обновление DynDNS из автоматизаций или скриптов

---

### 🛠 Разработка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Q14siX/home-assistant-dyndns-manager.git
   ```
2. Создайте новый файл провайдера в папке `custom_components/dyndns_manager/provider/`.
3. Реализуйте логику обновления по аналогии с другими провайдерами.

---

### 📬 Ошибки и поддержка

- **Сообщить об ошибках:** [GitHub Issues](https://github.com/Q14siX/home-assistant-dyndns-manager/issues)  
- **Документация:** [GitHub Readme](https://github.com/Q14siX/home-assistant-dyndns-manager)

---

### 📜 Лицензия

Этот проект распространяется по лицензии **MIT** — подробности в файле [LICENSE](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/LICENSE).
