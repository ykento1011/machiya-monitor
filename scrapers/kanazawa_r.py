import requests
from bs4 import BeautifulSoup

# 金沢R不動産のURL
URL = "https://www.realkanazawaestate.jp/"
# 一般的なブラウザのUser-Agentを設定
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def scrape_kanazawa_r():
    """
    金沢R不動産のサイトから物件リストを取得します。
    物件名は <b> タグで囲まれているため、これをキーに抽出します。
    """
    try:
        # User-Agentをヘッダーに含めてリクエスト
        response = requests.get(URL, headers=HEADERS, timeout=15) # タイムアウトも設定
        response.raise_for_status()
        response.encoding = response.apparent_encoding

        soup = BeautifulSoup(response.text, 'html.parser')
        
        b_tags = soup.find_all('b')
        
        items_list = [tag.get_text(strip=True) for tag in b_tags]
        
        # フッターなどに含まれる可能性のある "金沢R不動産" という文字列を含む項目は除外
        items_list = [item for item in items_list if "金沢R不動産" not in item]

        return list(set(items_list))

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {URL}: {e}")
        return []
