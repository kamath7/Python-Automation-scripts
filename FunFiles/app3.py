from pathlib import Path 

root_dir = Path('lalletext')
file_paths = list(root_dir.iterdir())

for path in file_paths:
    new_name = "new-"+path.stem+ path.suffix
    print("Filename will now be "+new_name)
    new_filepath = path.with_name(new_name)
    path.rename(new_filepath)
    