from pathlib import Path 

files_di = Path('files')

for filepath in files_di.iterdir():
    with open(filepath, 'r') as file: 
        content = file.read()
        new_cont = content.replace('amount', 'units')


    with open(filepath, 'w') as file:
        file.write(new_cont)