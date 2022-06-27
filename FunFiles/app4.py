from pathlib import Path 

root_dir = Path('myawesomedirectory')
# file_paths = root_dir.iterdir()
file_paths = root_dir.glob('**/*')
for path in file_paths:
    print(path)
