import re

pattern = re.compile('[^ ]+@[a-z]+.[a-z]+')

files = ['1.txt','2.txt','aa.txt']
emails = "this is lalle. oorlalea@a.com and another meail b@b.com"

matches = pattern.findall(emails)
print(matches)