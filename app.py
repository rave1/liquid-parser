import requests
import logging
from bs4 import BeautifulSoup
from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app)
logging.getLogger('flask_cors').level = logging.DEBUG


@app.route("/", methods = ['GET', 'POST'])
def parse_liquid():
    try:
        data = request.get_json()
        url = data['url']
        data = requests.get(url)

        soup = BeautifulSoup(data.text, features='html.parser')
        select = soup.find('select').text.strip().split('\n')


        title = soup.find('h1', itemprop='name').text
        picture = soup.find('img', alt=title)
        print(picture['data-src'])
        return {
            'data': {
                'available': select,
                'url': picture['data-src'],
                'title': title
            }
        }
    except KeyError:
        return {'data': None}

products = []

@app.route('/save', methods=['POST'])
def save_products():
    data = request.get_json()
    products.append(data)
    return products


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')