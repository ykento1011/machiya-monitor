import requests
from bs4 import BeautifulSoup

def scrape_hatomark():
    url = "https://www.hatomarksite.com/search/zentaku/rent/home/train/17/list?home_category%5B%5D=house&price_r_from=&price_r_to=&key_word=&building_area_all_from=&building_area_all_to=&building_area_all_unit=UNIT30&eki_walk=&wst%5B%5D=L5BB5WSB9"
    res = requests.get(url)
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text, 'html.parser')

    addresses = [
        div.text.strip()
        for div in soup.find_all("div", class_="address")
        if div.text.strip()
    ]
    return addresses
