import os 
from dotenv import load_dotenv
import requests

load_dotenv()

api_key = os.getenv('NEWS_KEY_API')

r = requests.get(f'https://newsapi.org/v2/everything?qInTitle=Manchester%20United&from=2022-5-16&to=2022-6-15&sortBy=popularity&language=en&apiKey={api_key}')
content = r.json()
my_articles = content['articles']
# for i in range(0, len(my_articles)):
#     print(f"${my_articles[i]['title']} -> ${my_articles[i]['description']} \n")

#better loop
# for article in my_articles:
#     print(article['title'],' | ', article['description'],'\n')

#personal news

def get_my_news(topic, from_date, to_date, language='en'):
    r = requests.get(f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language=en&apiKey={api_key}')
    content = r.json()
    my_articles = content['articles']
    for article in my_articles:
        print(article['title'],' | ', article['description'],'\n')


def top_headlines(country):
    r = requests.get(f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}')
    content = r.json()
    my_articles = content['articles']
    for article in my_articles:
        print(article['title'],' | ', article['description'],'\n')


get_my_news('Linkin Park','2022-06-01','2022-06-15')
top_headlines('in')
top_headlines('au')
