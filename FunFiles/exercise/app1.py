from pathlib import Path

root_dir = Path('files')
for path in root_dir.glob('**/*'):
    if path.is_file():
        parent_fol = path.parts 
        subfolde = path.parts[1:-1]

        new_filename = '-'.join(subfolde) + '-'+path.name 
        new_filepath = path.with_name(new_filename)
        path.rename(new_filepath)