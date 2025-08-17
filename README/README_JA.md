# DynDNS Manager

[![バージョン](https://img.shields.io/github/v/release/Q14siX/home-assistant-dyndns-manager)](https://github.com/Q14siX/home-assistant-dyndns-manager/releases)  
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
![言語](https://img.shields.io/badge/languages-20-blue.svg)  
![ステータス](https://img.shields.io/badge/status-stable-brightgreen.svg)  
![ダウンロード数](https://img.shields.io/github/downloads/Q14siX/home-assistant-dyndns-manager/total)

---

## 📌 Línguas / 语言 / 語言 / Jazyky / Sprog / Sprachen / Talen / Languages / Kielet / Langues / Nyelvek / Lingue / 言語 / Språk / Języki / Línguas / Языки / Idiomas / Språk / Diller
- [Brazilian Portuguese (pt-BR)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_PT-BR.md#portugues-brasileiro)
- Chinese (Simplified, zh-CN)
- Chinese (Traditional, zh-TW)
- [Czech (cs)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_CS.md#czech)
- [Danish (da)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_DA.md#dansk)
- [Deutsch (de)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_DE.md#deutsch)
- [Dutch (nl)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_NL.md#dutch)
- [English (en)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_EN.md#english)
- [Finnish (fi)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_FI.md#suomi)
- [French (fr)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_FR.md#français)
- [Hungarian (hu)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_HU.md#magyar)
- [Italian (it)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_IT.md#italiano)
- [**Japanese (ja)**](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_JA.md#日本語)
- [Norwegian (Bokmål, nb)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_NB.md#norsk)
- [Polish (pl)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_PL.md#polski)
- [Portuguese (pt)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_PT.md#português)
- [Russian (ru)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_RU.md#pусский)
- [Spanish (es)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_ES.md#español)
- [Swedish (sv)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_SV.md#svenska)
- [Turkish (tr)](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/README/README_TR.md#türkçe)

---

## 日本語

**DynDNS Manager** は [Home Assistant](https://www.home-assistant.io/) 用の使いやすい統合で、Home Assistant から直接 DynDNS プロバイダーの管理と更新を行えます。  
現在サポートしているプロバイダーは次のとおりです。

- **AllInkl**
- **Cloudflare**
- **DuckDNS**
- **NoIP**
- **Strato**

💡 さらに、**Fritz!Box** を DynDNS Manager に更新を送信するように設定できます。

この統合は次の機能を提供します。
- DynDNS レコードの自動更新
- Home Assistant の UI（Config Flow）による簡単な設定
- 複数プロバイダーの同時サポート
- Home Assistant のボタンからの手動更新
- Home Assistant サービスを介した DynDNS 更新の直接実行（自動化やスクリプト向け）

---

### 🚀 インストール

#### 🔹 HACS 経由のインストール（推奨）

1. Home Assistant で **HACS** を開きます。
2. **統合** に進みます。
3. 右上の **3 点メニュー** をクリックして **カスタムリポジトリを追加** を選択します。
4. 次のリポジトリを追加します。

   ```
   https://github.com/Q14siX/home-assistant-dyndns-manager
   ```

   カテゴリ: **Integration**

5. HACS で **DynDNS Manager** を検索してインストールします。
6. Home Assistant を再起動します。

---

#### 🔹 手動インストール

1. [GitHub Releases](https://github.com/Q14siX/home-assistant-dyndns-manager/releases) から最新バージョンをダウンロードします。
2. ZIP ファイルを解凍します。
3. `custom_components` 配下の **`dyndns_manager`** フォルダを、Home Assistant の `custom_components` フォルダにコピーします。

   ```bash
   cp -r custom_components/dyndns_manager /config/custom_components/
   ```

4. Home Assistant を再起動します。

---

### ⚙️ Home Assistant での設定

1. Home Assistant で **設定 → デバイスとサービス** に移動します。
2. **統合を追加** をクリックします。
3. **DynDNS Manager** を検索します。
4. 希望するプロバイダー（DuckDNS、Strato、Cloudflare、NoIP、ALL-INKL）を選択します。
5. 必要な資格情報 / API キーを入力します。
6. 完了です。DynDNS レコードは自動的に更新されるようになります。

---

### 📄 構成

#### サポートされているプロバイダーと必要なデータ

| プロバイダー | 必要なデータ |
|--------------|--------------|
| ALL-INKL     | ユーザー名、パスワード、ドメイン |
| Cloudflare   | API トークン、Zone ID、ドメイン |
| DuckDNS      | API トークン、ドメイン |
| NoIP         | ユーザー名、パスワード、ドメイン |
| Strato       | ユーザー名、パスワード、ドメイン |

すべての入力は Home Assistant の **Config Flow** から簡単に行えます。`configuration.yaml` を変更する必要はありません。

---

### 📡 Fritz!Box 連携

この統合は Fritz!Box からの更新も受け取れます。

Fritz!Box の **Internet → Freigaben（共有）→ Dynamic DNS** に次の URL を入力します。

```
http://<ha_host>:<ha_port>/dyndns-manager/?username=<username>&password=<pass>&ipv4=<ipaddr>&ipv6=<ip6addr>
```

- `<ha_host>` → Home Assistant のホスト名または IP アドレス
- `<ha_port>` → Home Assistant のポート（既定: 8123）
- `<username>` / `<pass>` → Web アクセス用の認証情報（セットアップウィザード参照）
- `<ipaddr>` / `<ip6addr>` → IPv4 / IPv6 のプレースホルダー

💡 **注意:** Fritz!Box では `<ha_host>` と `<ha_port>` だけを変更すれば十分です。その他の値（`<username>`、`<pass>`、`<ipaddr>`、`<ip6addr>`）は、フォーム入力時に Fritz!Box が自動的に置き換えます。

![FRITZ!BOX 入力フォーム](https://raw.githubusercontent.com/Q14siX/home-assistant-dyndns-manager/master/images/FRITZ!Box.png)

---

### 🔘 Home Assistant の機能

- **センサー** → 現在のステータスと IP アドレスを表示
- **ボタン** → IP の手動更新を実行
- **サービス** → 自動化やスクリプトから直接 DynDNS 更新を実行可能

---

### 🛠 開発

1. リポジトリをクローンします。
   ```bash
   git clone https://github.com/Q14siX/home-assistant-dyndns-manager.git
   ```
2. `custom_components/dyndns_manager/provider/` フォルダに新しいプロバイダーファイルを作成します。
3. 既存のプロバイダーを参考に更新ロジックを実装します。

---

### 📬 不具合とサポート

- **問題を報告:** [GitHub Issues](https://github.com/Q14siX/home-assistant-dyndns-manager/issues)  
- **ドキュメント:** [GitHub Readme](https://github.com/Q14siX/home-assistant-dyndns-manager)

---

### 📜 ライセンス

本プロジェクトは **MIT ライセンス** です。詳細は [LICENSE](https://github.com/Q14siX/home-assistant-dyndns-manager/blob/main/LICENSE) を参照してください。
