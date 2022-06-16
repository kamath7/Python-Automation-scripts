import os 
from dotenv import load_dotenv
import requests

load_dotenv()

api_key = os.getenv('NEWS_KEY_API')

r = requests.get(f'https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2022-5-16&to=2022-6-15&sortBy=popularity&language=en&apiKey={api_key}')
content = r.json()
print(content)