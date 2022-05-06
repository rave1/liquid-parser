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

@app.route('/save', methods=['POST'])
def save_products():
    data = request.get_json()
    return data


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')