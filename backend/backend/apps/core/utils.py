from bs4 import BeautifulSoup
import requests


def parse_liquid(url):

    data = requests.get(url)

    soup = BeautifulSoup(data.text, features='html.parser')
    select = soup.find('select').text.strip().split('\n')

    title = soup.find('h1', itemprop='name').text
    picture = soup.find('img', alt=title)
    print(picture['data-src'])
    return {
        'available': select,
        'picture': picture['data-src'],
        'title': title,
        'url': url
    }
