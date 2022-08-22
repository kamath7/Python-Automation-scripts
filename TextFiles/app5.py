from pathlib import Path 

files_d = Path('files')
for filepath in files_d.iterdir():
    with open(filepath, 'r') as file:
        con = file.read()
        new_con = con[:-1]

    with open(filepath, 'w') as file:
        file.write(new_con)