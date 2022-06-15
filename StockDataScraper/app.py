import requests
from datetime import datetime
import time 

def convert_to_epoch(text):
    return int(time.mktime(datetime.strptime(text, '%Y/%m/%d').timetuple()))

from_date = input("Enter start date (yyyy/mm/dd): ")
to_date = input("Enter end date (yyyy/mm/dd): ")
ticker = input("Enter ticker (MSFT/AMZN/GOOG/APPL/META")

from_date = convert_to_epoch(from_date)
to_date = convert_to_epoch(to_date)

url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_date}&period2={to_date}&interval=1d&events=history&includeAdjustedClose=true"
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"} 
content = requests.get(url, headers=headers).content

with open("data.csv", 'wb') as file:
    file.write(content)