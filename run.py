import os
import json
from scrapers.kotonoha import scrape_kotonoha
from scrapers.kanazawa_bank import scrape_kanazawa_bank
from scrapers.eiwa_land import scrape_eiwa_land
from scrapers.tenant_noka import scrape_tenant_noka
from scrapers.hatomark import scrape_hatomark
from scrapers.kanazawa_r import scrape_kanazawa_r  # ← この行を追
from scrapers.pacific import scrape_pacific  # ← この行を追加
from notifier.discord import send_to_discord

def load_previous(path):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_current(path, messages):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)

def main():
    all_sources = [
        ("kotonoha", scrape_kotonoha, "data/kotonoha_prev.json"),
        ("kanazawa_bank", scrape_kanazawa_bank, "data/kanazawa_bank_prev.json"),
        ("eiwa_land", scrape_eiwa_land, "data/eiwa_land_prev.json"),
        ("tenant_noka", scrape_tenant_noka, "data/tenant_noka_prev.json"),
        ("hatomark", scrape_hatomark, "data/hatomark_prev.json"),
        ("kanazawa_r", scrape_kanazawa_r, "data/kanazawa_r_prev.json"), # ← この行を追加
         ("pacific", scrape_pacific, "data/pacific_prev.json"), # ← この行を追加
    ]

    for site_name, scraper_func, data_path in all_sources:
        current = scraper_func()

        # === ↓ここからデバッグ用のコードを追加 ===
        # 取得したリストの中身をログに出力して確認
        print(f"[{site_name}] Fetched items count: {len(current)}")
        # リストが長すぎる場合を考慮し、最初の5件だけ表示するなどの工夫も有効
        print(f"[{site_name}] Fetched items (sample): {current[:5]}") 
        # === ↑ここまでデバッグ用のコードを追加 ===
        
        previous = load_previous(data_path)
        new_items = [msg for msg in current if msg not in previous]

        if new_items:
            send_to_discord(site_name, new_items)

        save_current(data_path, current)

if __name__ == "__main__":
    main()