from pathlib import Path 

files_dir = Path('files')

merge = ''

for index, filepath in enumerate(files_dir.iterdir()):
    with open(filepath, 'r') as file:
        content = file.readlines()
        new_cont = content[1:]
    if index == 0:
        content = ''.join(content)
        merge = merge + content + "\n"
    else:
        new_cont = ''.join(new_cont)
        merge = merge + new_cont + '\n'

    

with open("merged.csv","w") as file:
    file.write(merge)
