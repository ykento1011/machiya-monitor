import requests
from bs4 import BeautifulSoup

def scrape_tenant_noka():
    url = "https://tenant.noka.co.jp/property"
    res = requests.get(url)
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text, 'html.parser')

    titles = [
        div.text.strip()
        for div in soup.find_all("div", class_="title")
        if div.text.strip()
    ]
    return titles