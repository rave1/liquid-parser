import requests
from bs4 import BeautifulSoup
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route("/", methods = ['GET', 'POST'])
def parse_liquid():
    data = request.get_json()
    url = data['url']
    data = requests.get(url)

    soup = BeautifulSoup(data.text, features='html.parser')
    select = soup.find('select').text.strip().split('\n')
    picture = soup.find('a', class_='js-easyzoom-trigger').get('href')
    title = soup.find('h1', itemprop='name').text
    return {
        'data': {
            'available': select,
            'url': picture,
            'title': title
        }
    }