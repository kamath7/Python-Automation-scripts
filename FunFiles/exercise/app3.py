from pathlib import Path
from datetime import datetime


root_dir = Path('files')
for path in root_dir.glob('**/*'):
    if path.is_file():
        stats = path.stat()
        sec_created = stats.st_ctime
        date_created_name = datetime.fromtimestamp(sec_created).strftime("%Y-%m-%d_%H:%M:%S")
        new_filename = date_created_name +'-'+ path.name
        new_filepath = path.with_name(new_filename)
        path.rename(new_filepath)