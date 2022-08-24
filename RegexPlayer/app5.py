from pathlib import Path
import re 

root_dir = Path('files')
filenames = root_dir.iterdir()

filenames_str = [filename.name for filename in filenames]
print(filenames_str)

pattern = re.compile("nov[a-z]*-(?.[1-9]|1[0-9]|20)",re.IGNORECASE)
matches = [filename for filename in filenames if pattern.findall(filename)]