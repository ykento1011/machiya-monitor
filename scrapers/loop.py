import requests
from bs4 import BeautifulSoup

# LOOP不動産のURL
URL = "https://asp.athome.jp/067350/shumoku/chintai/search_type/area/bukken?&ken_cd%5B%5D=17&ken_cd%5B%5D=18&lp=200&shozaichi_cd%5B%5D=UENaX1w"
# 一般的なブラウザのUser-Agentを設定
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def scrape_loop():
    """
    LOOP不動産(at-home)のサイトから物件リストを取得します。
    物件名はクラス名「searchResults_name」を持つpタグの中のaタグから抽出します。
    """
    try:
        response = requests.get(URL, headers=HEADERS, timeout=15)
        response.raise_for_status()
        response.encoding = response.apparent_encoding

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 物件タイトルが含まれるaタグをCSSセレクタで正確に指定
        selector = "p.searchResults_name a"
        title_tags = soup.select(selector)
        
        # タグからテキストを抽出し、リストに格納
        items_list = [tag.get_text(strip=True) for tag in title_tags]

        return list(set(items_list))

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {URL}: {e}")
        return []

# テスト用
if __name__ == '__main__':
    items = scrape_loop()
    if items:
        print("--- 取得した物件タイトル一覧 ---")
        for item in items:
            print(item)
    else:
        print("物件が取得できませんでした。")