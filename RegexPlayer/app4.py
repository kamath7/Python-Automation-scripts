import re
with open('lalleips.txt','r') as file:
    content = file.read()
print(content)

pattern = re.compile('[0-9]{3}\.[0-9]{3}\.[0-9]{3}')
matches = pattern.findall(content)
print(matches)