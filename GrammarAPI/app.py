import json
from urllib import response
import requests


url = f"https://api.languagetool.org/v2/check"

data = {
    "text": "sitty daey",
    "language": "en-US"
}

r = requests.post(url=url,data=data)
# print(r.text)

result = json.loads(r.text)
print(result)