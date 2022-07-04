from pathlib import Path

root_d = Path('files2')

for path in root_d.rglob("*.txt"):
    if path.is_file():
        new_filepath = path.with_suffix(".xlsx")
        path.rename(new_filepath)