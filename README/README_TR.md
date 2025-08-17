# DynDNS Manager

[![Sürüm](https://img.shields.io/github/v/release/Q14siX/home-assistant-dyndns-manager)](https://github.com/Q14siX/home-assistant-dyndns-manager/releases)  
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
![Diller](https://img.shields.io/badge/languages-20-blue.svg)  
![Durum](https://img.shields.io/badge/status-stable-brightgreen.svg)  
![İndirmeler](https://img.shields.io/github/downloads/Q14siX/home-assistant-dyndns-manager/total)

---

[![Buy Me A Coffee](https://img.buymeacoffee.com/button-api/?text=Stefan%27a%20lezzetli%20bir%20kahve%20al&emoji=☕&slug=q14six&button_colour=FFDD00&font_colour=000000&font_family=Lato&outline_colour=000000&coffee_colour=ffffff)](https://buymeacoffee.com/q14six)

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
- [Russian (ru)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_RU.md#Русский)
- [Spanish (es)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_ES.md#español)
- [Swedish (sv)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_SV.md#svenska)
- [**Turkish (tr)**](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_TR.md#türkçe)

---

## Türkçe

**DynDNS Manager**, [Home Assistant](https://www.home-assistant.io/) için kullanıcı dostu bir entegrasyondur; DynDNS sağlayıcılarınızı doğrudan Home Assistant üzerinden yönetip güncellemenizi sağlar.  
Entegrasyon şu anda aşağıdaki sağlayıcıları desteklemektedir:

- **AllInkl**
- **Cloudflare**
- **DuckDNS**
- **NoIP**
- **Strato**

💡 Ayrıca bir **Fritz!Box**, DynDNS Manager’a güncellemeler gönderecek şekilde yapılandırılabilir.

Entegrasyon şunları sunar:
- DynDNS kayıtlarının otomatik güncellenmesi
- Home Assistant arayüzünde (Config Flow) kolay kurulum sihirbazı
- Aynı anda birden fazla sağlayıcı desteği
- Home Assistant düğmeleriyle doğrudan manuel güncelleme
- Home Assistant hizmeti üzerinden doğrudan DynDNS güncellemesi çalıştırma (otomasyonlar ve betikler için)

---

### 🚀 Kurulum

#### 🔹 HACS üzerinden kurulum (önerilir)

1. Home Assistant’ınızda **HACS**’ı açın.
2. **Entegrasyonlar** bölümüne gidin.
3. Sağ üstteki **3 nokta**ya tıklayıp **Özel depo ekle**yi seçin.
4. Aşağıdaki depoyu ekleyin:

   ```
   https://github.com/Q14siX/home-assistant-dyndns-manager
   ```

   Kategori: **Integration / Entegrasyon**

5. HACS içinde **DynDNS Manager**’ı arayıp yükleyin.
6. Home Assistant’ı yeniden başlatın.

---

#### 🔹 Manuel kurulum

1. En son sürümü [GitHub Releases](https://github.com/Q14siX/home-assistant-dyndns-manager/releases) sayfasından indirin.
2. ZIP dosyasını çıkarın.
3. `custom_components` altındaki **`dyndns_manager`** klasörünü Home Assistant’ınızın `custom_components` klasörüne kopyalayın:

   ```bash
   cp -r custom_components/dyndns_manager /config/custom_components/
   ```

4. Home Assistant’ı yeniden başlatın.

---

### ⚙️ Home Assistant’ta yapılandırma

1. Home Assistant’ta **Ayarlar → Cihazlar ve hizmetler** menüsüne gidin.
2. **Entegrasyon ekle**ye tıklayın.
3. **DynDNS Manager**’ı arayın.
4. İstediğiniz sağlayıcıyı seçin (DuckDNS, Strato, Cloudflare, NoIP veya ALL-INKL).
5. Gerekli kimlik bilgilerini / API anahtarlarını girin.
6. Bitti! DynDNS kayıtlarınız artık otomatik olarak güncellenecek.

---

### 📄 Konfigürasyon

#### Desteklenen sağlayıcılar ve gerekli veriler

| Sağlayıcı  | Gerekli veriler |
|------------|-----------------|
| ALL-INKL   | Kullanıcı adı, parola, alan adı |
| Cloudflare | API belirteci, Zone ID, alan adı |
| DuckDNS    | API belirteci, alan adı |
| NoIP       | Kullanıcı adı, parola, alan adı |
| Strato     | Kullanıcı adı, parola, alan adı |

Tüm bilgiler **Config Flow** üzerinden Home Assistant arayüzünde kolayca girilir — `configuration.yaml` dosyasında değişiklik yapmanız gerekmez.

---

### 📡 Fritz!Box bağlantısı

Entegrasyon, Fritz!Box’tan gelen güncellemeleri de alabilir.

Fritz!Box’ta **Internet → Paylaşımlar (Freigaben) → Dynamic DNS** altında aşağıdaki URL’yi girin:

```
http://<ha_host>:<ha_port>/dyndns-manager/?username=<username>&password=<pass>&ipv4=<ipaddr>&ipv6=<ip6addr>
```

- `<ha_host>` → Home Assistant sunucunuzun ana bilgisayar adı veya IP adresi
- `<ha_port>` → Home Assistant portu (varsayılan: 8123)
- `<username>` / `<pass>` → web erişimi kimlik bilgileri (kurulum sihirbazına bakın)
- `<ipaddr>` / `<ip6addr>` → IPv4 ve/veya IPv6 için yer tutucular

💡 **Not:** Fritz!Box’ta yalnızca `<ha_host>` ve `<ha_port>` değerlerini değiştirmeniz yeterlidir. Diğer değerler (`<username>`, `<pass>`, `<ipaddr>`, `<ip6addr>`) formu doldurduğunuzda Fritz!Box tarafından otomatik olarak doldurulur.

![FRITZ!BOX giriş formu](https://raw.githubusercontent.com/Q14siX/home-assistant-dyndns-manager/master/images/FRITZ!Box.png)

---

### 🔘 Home Assistant’ta işlevler

- **Sensörler** → mevcut durumu ve IP adresini gösterir
- **Düğmeler** → IP’nin manuel olarak güncellenmesini sağlar
- **Hizmet** → otomasyonlar veya betiklerden doğrudan DynDNS güncellemesi çalıştırmayı sağlar

---

### 🛠 Geliştirme

1. Depoyu klonlayın:
   ```bash
   git clone https://github.com/Q14siX/home-assistant-dyndns-manager.git
   ```
2. `custom_components/dyndns_manager/provider/` klasöründe yeni bir sağlayıcı dosyası oluşturun.
3. Diğer sağlayıcıları örnek alarak güncelleme mantığını uygulayın.

---

### 📬 Hatalar ve destek

- **Sorun bildir:** [GitHub Issues](https://github.com/Q14siX/home-assistant-dyndns-manager/issues)  
- **Dokümantasyon:** [GitHub Readme](https://github.com/Q14siX/home-assistant-dyndns-manager)

---

### 📜 Lisans

Bu proje **MIT lisansı** ile lisanslanmıştır — ayrıntılar için [LICENSE](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/LICENSE) dosyasına bakın.
