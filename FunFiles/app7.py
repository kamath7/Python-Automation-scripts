from pathlib import Path 
import zipfile

root_dir = Path('.')
dest_path = Path("destinationZip")

for path in root_dir.glob("*.zip"):
    with zipfile.ZipFile(path, 'r') as zf:
        final_path = dest_path / Path (path.stem)
        zf.extractall(path = final_path)