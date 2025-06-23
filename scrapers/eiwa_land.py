import requests
from bs4 import BeautifulSoup

def scrape_eiwa_land():
    url = "https://www.eiwa-land.co.jp/list/?kind=rent"
    res = requests.get(url)
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text, 'html.parser')

    titles = [
        a.text.strip()
        for a in soup.select("table.p-list_info__table td a")
        if a.text.strip()
    ]
    return titles
