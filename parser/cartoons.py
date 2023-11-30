import requests
from bs4 import BeautifulSoup as BS
# from pprint import pprint
URL = 'https://rezka.ag/cartoons/'
# import datetime

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5.1 Safari/605.1.15"
}


def get_html(url, params='filter=watching'):
    req = requests.get(url=url, headers=HEADERS, params=params)
    return req

def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='b-content__inline_item')
    cartoons = []
    for item in items:
        info = item.find('div', class_='b-content__inline_item-link').find('div').string.split(', ')
        cartoon = {
            # 'title': item.find('div', class_='b-content__inline_item-link').find('a').getText()
            'title': item.find('div', class_='b-content__inline_item-link').find('a').string,
            'link': item.find('div', class_='b-content__inline_item-link').find('a').get('href'), # get() достает атрибут
            'status': item.find('span', class_='info').string 
            if item.find('span', class_='info') is not None else "Полнометражка",
        }
        try:
            cartoon['year'] = info[0]
            cartoon['country'] = info[1]
            cartoon['genre'] = info[2]
        except IndexError:
            cartoon['year'] = info[0]
            cartoon['country'] = "unknown"
            cartoon['genre'] = info[1]
        cartoons.append(cartoon)
    return cartoons


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        cartoons = []
        for i in range(1,2):
            html = get_html(f"{URL}page/{i}/")
            current_page = get_data(html.text)
            cartoons.extend(current_page)
        return cartoons
    else:
        raise Exception("Error in parser!")
    


# start = datetime.datetime.now()
# a = parser()
# print(len(a))
# pprint(a)
# print(datetime.datetime.now()- start)
# print(len(a))
