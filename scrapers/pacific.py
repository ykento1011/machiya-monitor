import requests
from bs4 import BeautifulSoup

# パシフィック不動産のURL
URL = "https://pacific-re.jp/type/rent/"
# 一般的なブラウザのUser-Agentを設定
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def scrape_pacific():
    """
    パシフィック不動産のサイトから物件リストを取得します。
    物件名はクラス名「bl_searchResultBlock_item_text_ttl」を持つdivタグから抽出します。
    """
    try:
        response = requests.get(URL, headers=HEADERS, timeout=15)
        response.raise_for_status()
        response.encoding = response.apparent_encoding

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 物件タイトルが含まれるdivタグをCSSセレクタで正確に指定
        selector = "div.bl_searchResultBlock_item_text_ttl"
        title_tags = soup.select(selector)
        
        # タグからテキストを抽出し、リストに格納
        items_list = [tag.get_text(strip=True) for tag in title_tags]

        # 重複を削除して返す
        return list(set(items_list))

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {URL}: {e}")
        return []

# テスト用
if __name__ == '__main__':
    items = scrape_pacific()
    if items:
        print("--- 取得した物件タイトル一覧 ---")
        for item in items:
            print(item)
    else:
        print("物件が取得できませんでした。")