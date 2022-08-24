from distutils.filelist import findall
import re

with open('sometx.txt','r') as file:
    content = file.read()

print(content)

pattern = re.compile('http?://(?:www.)?[^ \n]*\.com')
matches = pattern.findall(content)
print(matches)