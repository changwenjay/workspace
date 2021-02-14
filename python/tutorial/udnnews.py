import requests
from bs4 import BeautifulSoup

def udn_hot_news():
    url = 'https://udn.com/news/index'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    result = soup.select('.tab-link__title')

    ret = []
    for x in result:
        ret.append(x.text)
    
    return ret

if __name__ == '__main__':
    result = udn_hot_news()
    for x in result:
        print(x)

