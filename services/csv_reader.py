import csv
from pathlib import Path


def read_files(file_paths: list[str]) -> list[dict]:
    rows: list[dict] = []

    for path in file_paths:
        file_path = Path(path)

        if not file_path.exists():
            raise FileNotFoundError(f"файл не найден: {path}")

        with file_path.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                rows.append(row)

    return rows
