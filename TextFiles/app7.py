from pathlib import Path 

files_dir = Path('files')

merge = ''

for filepath in files_dir.iterdir():
    with open(filepath, 'r') as file:
        content = file.read()
    merge = merge + content + "\n"

with open("merged.csv","w") as file:
    file.write(merge)
