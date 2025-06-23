import requests
from bs4 import BeautifulSoup

def scrape_kotonoha():
    url = "https://www.kotonohaweb.com/"
    res = requests.get(url)
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text, 'html.parser')

    # <h3 class="front-post__body__item__ttl">の内容をすべて抽出
    titles = [
        h3.text.strip()
        for h3 in soup.find_all("h3", class_="front-post__body__item__ttl")
        if h3.text.strip()
    ]
    return titles
