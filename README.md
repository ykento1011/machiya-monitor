> ⚠️ 本ツールは個人利用・技術検証目的で作成された非公式のスクレイピングツールです。  
> 掲載されている各不動産サイト様とは一切関係ありません。

# 🏠 machiya-monitor

金沢市の町家・貸家・貸店舗などの物件情報を、複数の不動産サイトから定期的にスクレイピングして、**差分のみをDiscord通知**する自動モニターツールです。

---

## 🚀 機能概要

- 対応サイト（2025年6月時点）：
  - [ことのは不動産](https://www.kotonohaweb.com/)
  - [金澤町家情報バンク](https://bank.kanazawa-machiyajouho.jp/)
  - [永和地所](https://www.eiwa-land.co.jp/)
  - [金沢テナントナビ（のうか不動産）](https://tenant.noka.co.jp/property)
  - LOOP不動産 (at-home)
  - パシフィック不動産
  - 金沢R不動産

- 差分（新着物件）検出ロジック
- Discord Webhook 通知（1日3回）
- GitHub Actions による自動実行（JST: 9時 / 13時 / 18時）

---

## 📦 ディレクトリ構成

machiya-monitor/
├── scrapers/ # 各サイトごとのスクレイパー
├── data/ # 過去データ（差分検出用）
├── notifier/ # Discord通知ロジック
├── run.py # メイン実行スクリプト
├── requirements.txt # 必要なPythonパッケージ
└── .github/workflows/ # GitHub Actions スケジューラ


---

## 🔧 セットアップ方法（開発用）

```bash
# パッケージインストール
pip install -r requirements.txt

# 実行（手動）
export DISCORD_WEBHOOK_URL=YOUR_WEBHOOK_URL
python run.py

🛠 GitHub Actions での自動実行
.github/workflows/scrape.yml により、1日3回定期実行

DISCORD_WEBHOOK_URL は GitHub Secrets に登録

実行ログと通知動作は Actions タブで確認可能

📬 通知例（Discord）
📢 [kotonoha] 新しい物件タイトル一覧：
金沢市長町3 貸店舗
🔗 サイトを見る: https://www.kotonohaweb.com/

