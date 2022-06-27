#Conventional way
from pathlib import Path

p1 = Path('./abc.txt')
p2 = Path('./gef.txt')

if p1.exists():
    with open('abc.txt') as f1:
        print(f1.read())

if not p2.exists():
    with open(p2,'w') as f1:
        f1.write('written through pathlib')

print(p1.name)
