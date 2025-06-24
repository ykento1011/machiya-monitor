import os
import requests

WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL") 

SOURCE_URLS = {
    "kotonoha": "https://www.kotonohaweb.com/",
    "kanazawa_bank": "https://bank.kanazawa-machiyajouho.jp/search/",
    "eiwa_land": "https://www.eiwa-land.co.jp/estate/chintai/",
    "tenant_noka": "https://tenant.noka.co.jp/property",
    "hatomark": "https://www.hatomarksite.com/search/zentaku/rent/home/train/17/list?home_category%5B%5D=house&price_r_from=&price_r_to=&key_word=&building_area_all_from=&building_area_all_to=&building_area_all_unit=UNIT30&eki_walk=&wst%5B%5D=L5BB5WSB9"
}

def send_to_discord(site, messages):
    if not messages:
        return
    content = f"**📢 [{site}] 新しい物件タイトル一覧：**\n" + "\n".join(f"- {msg}" for msg in messages)
    if site in SOURCE_URLS:
        content += f"\n\n🔗 [サイトを見る]({SOURCE_URLS[site]})"
    requests.post(WEBHOOK_URL, json={"content": content})

    # This workflow is triggered by schedule and manual dispatch
