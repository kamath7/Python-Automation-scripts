import os 
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('NEWS_KEY_API')
print(api_key)