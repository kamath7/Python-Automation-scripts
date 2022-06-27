from pathlib import Path 

p2 = Path('lalletext')
print(p2.iterdir())

print(list(p2.iterdir()))

for item in p2.iterdir():
    print(type(item))