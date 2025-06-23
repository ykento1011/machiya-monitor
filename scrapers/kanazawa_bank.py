import requests
from bs4 import BeautifulSoup

def scrape_kanazawa_bank():
    url = "https://bank.kanazawa-machiyajouho.jp/search/"
    res = requests.get(url)
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text, 'html.parser')

    titles = [
        p.text.strip()
        for p in soup.find_all("p", class_="name")
        if p.text.strip()
    ]
    return titles
