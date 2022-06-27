from pathlib import Path 

root_dir = Path('lalletext')

for i in range(60,70):
    filename = str(i) + '.txt'
    filepath = root_dir / Path(filename)
    filepath.touch()