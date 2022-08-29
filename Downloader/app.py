import requests

r = requests.get(url="https://filesamples.com/samples/document/csv/sample4.csv")
content = r.content

with open('myawesome.csv','wb') as file:
    file.write(content)