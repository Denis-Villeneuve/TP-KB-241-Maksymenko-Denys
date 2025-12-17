import json
from typing import Any, List


class FileManager:
    @staticmethod
    def read_json(path: str) -> List[Any]:
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, list):
                return data
            return []
        except FileNotFoundError:
            # якщо файлу немає — повертаємо порожній список
            return []

    @staticmethod
    def write_json(path: str, data: List[Any]) -> None:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)