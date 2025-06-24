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
    物件タイトルのみをCSSセレクタで正確に抽出します。
    """
    try:
        response = requests.get(URL, headers=HEADERS, timeout=15)
        response.raise_for_status()
        response.encoding = response.apparent_encoding

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 物件タイトルのみをCSSセレクタで正確に指定して取得
        # 「div id="estate_box"の中の、styleに"font-size:13px"を含むspanの中の、bタグ」
        selector = 'div#estate_box span[style*="font-size:13px"] b'
        title_tags = soup.select(selector)
        
        # タグからテキストを抽出し、リストに格納
        items_list = [tag.get_text(strip=True) for tag in title_tags]

        # 重複を削除して返す
        return list(set(items_list))

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {URL}: {e}")
        return []

# テスト用（このファイル単体で実行すると、取得結果をコンソールに出力します）
if __name__ == '__main__':
    items = scrape_kanazawa_r()
    if items:
        print("--- 取得した物件タイトル一覧 ---")
        for item in items:
            print(item)
    else:
        print("物件が取得できませんでした。")