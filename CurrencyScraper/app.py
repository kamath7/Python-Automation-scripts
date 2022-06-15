from bs4 import BeautifulSoup
import requests

def cleaner_text(text):
    return float(text.split(" ")[0])

def get_curr(in_currency, out_currency):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    curr_rate = soup.find('span', class_="ccOutputRslt").get_text()
    print(cleaner_text(curr_rate))

get_curr('EUR','USD')
get_curr("USD","INR")
