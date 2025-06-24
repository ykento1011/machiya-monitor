import os
import requests

# DiscordのWebhook URLを環境変数から取得
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL") 

# 各サイトのURLをまとめた辞書
SOURCE_URLS = {
    "kotonoha": "https://www.kotonohaweb.com/",
    "kanazawa_bank": "https://bank.kanazawa-machiyajouho.jp/search/",
    "eiwa_land": "https://www.eiwa-land.co.jp/estate/chintai/",
    "tenant_noka": "https://tenant.noka.co.jp/property",
    "hatomark": "https://www.hatomarksite.com/search/zentaku/rent/home/train/17/list?home_category%5B%5D=house&price_r_from=&price_r_to=&key_word=&building_area_all_from=&building_area_all_to=&building_area_all_unit=UNIT30&wst%5B%5D=L5BB5WSB9",
    "kanazawa_r": "https://www.realkanazawaestate.jp/", # ← この行を追加しました
    "pacific": "https://pacific-re.jp/type/rent/", # ← この行を追加
}

def send_to_discord(site, messages):
    """
    新しい物件情報をDiscordに通知します。
    """
    if not messages:
        return

    # 通知メッセージを作成
    content = f"**📢 [{site}] 新しい物件タイトル一覧：**\n" + "\n".join(f"- {msg}" for msg in messages)
    
    # もしサイトのURLが辞書にあれば、リンクを追加
    if site in SOURCE_URLS:
        content += f"\n\n🔗 [サイトを見る]({SOURCE_URLS[site]})"
    
    # WebhookにPOSTリクエストを送信
    try:
        response = requests.post(WEBHOOK_URL, json={"content": content}, timeout=10)
        response.raise_for_status() # エラーがあれば例外を発生
    except requests.exceptions.RequestException as e:
        print(f"Failed to send message to Discord for site {site}: {e}")