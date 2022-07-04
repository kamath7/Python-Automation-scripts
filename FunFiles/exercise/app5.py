from pathlib import Path 

root_d = Path('files3')
search_t = input("Enter filename without extension ")

for path in root_d.rglob("*"):
    if search_t in path.stem:
        print(path.absolute())
    else:
        print("File doesn't exist")
        break