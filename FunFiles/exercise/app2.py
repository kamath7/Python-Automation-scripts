from pathlib import Path 
from datetime import datetime

path = Path('files/2021/November/a.txt')
stats = path.stat()
sec_created = stats.st_ctime
date_created = datetime.fromtimestamp(sec_created).strftime("%Y-%m-%d_%H:%M:%S")

print(stats)
print(date_created)