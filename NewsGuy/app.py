import os 
from dotenv import load_dotenv
import requests

load_dotenv()

api_key = os.getenv('NEWS_KEY_API')

r = requests.get(f'https://newsapi.org/v2/everything?qInTitle=Manchester%20United&from=2022-5-16&to=2022-6-15&sortBy=popularity&language=en&apiKey={api_key}')
content = r.json()
my_articles = content['articles']
for i in range(0, len(my_articles)):
    print(f"${my_articles[i]['title']} -> ${my_articles[i]['description']} \n")
