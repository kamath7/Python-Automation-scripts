from pathlib import Path 

root_dir = Path('myawesomedirectory')
# file_paths = root_dir.iterdir()
file_paths = root_dir.glob('**/*')
for path in file_paths:
    if path.is_file():
        parent_fol = path.parts[-2] #splits path ('myawesomedi','lalle1','1.txt')
        new_filename = parent_fol + 'morelalle' + path.name
        print(new_filename)
        new_filepath = path.with_name(new_filename)
        path.rename(new_filepath)