from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests
#helper funcs


def cleaner_text(text):
    return float(text.split(" ")[0])

def get_curr(in_currency, out_currency):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    curr_rate = soup.find('span', class_="ccOutputRslt").get_text()
    # print(cleaner_text(curr_rate))
    return cleaner_text(curr_rate)


app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello This is Flask speaking! Use /api/v1 for </h1>'

@app.route('/api/v1/<in_curr>-<out_curr>')
def my_api(in_curr, out_curr):
    rate = get_curr(in_curr,out_curr)
    result = {
        'input_currency':in_curr,
        'output_currency':out_curr,
        'rate': rate
    }
    return jsonify(result)
    



app.run()