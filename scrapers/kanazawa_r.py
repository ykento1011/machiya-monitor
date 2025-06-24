import requests
from bs4 import BeautifulSoup

# 金沢R不動産のURL
URL = "https://www.realkanazawaestate.jp/"

def scrape_kanazawa_r():
    """
    金沢R不動産のサイトから物件リストを取得します。
    物件名は <b> タグで囲まれているため、これをキーに抽出します。
    """
    try:
        response = requests.get(URL)
        response.raise_for_status()
        response.encoding = response.apparent_encoding

        soup = BeautifulSoup(response.text, 'html.parser')
        
        b_tags = soup.find_all('b')
        
        items_list = [tag.get_text(strip=True) for tag in b_tags]
        
        # フッターなどに含まれる可能性のある "金沢R不動産" という文字列を含む項目は除外
        items_list = [item for item in items_list if "金沢R不動産" not in item]

        # 重複を削除して返す
        return list(set(items_list))

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {URL}: {e}")
        return []

# テスト用（このファイル単体で実行すると、取得結果をコンソールに出力します）
if __name__ == '__main__':
    items = scrape_kanazawa_r()
    if items:
        for item in items:
            print(item)