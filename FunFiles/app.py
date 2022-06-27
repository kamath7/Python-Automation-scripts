#Conventional way
from pathlib import Path

p1 = Path('./abc.txt')

if p1.exists():
    with open('abc.txt') as f1:
        print(f1.read())