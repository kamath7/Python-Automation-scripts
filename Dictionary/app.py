import json

file = open('data.json')
data = json.load(file)

def inp(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return "Please check what you have entered"


search = input("What are you looking for? ")
print(inp(search))
file.close()