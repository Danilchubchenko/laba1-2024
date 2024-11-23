import re
from dataclasses import dataclass
from typing import Dict

@dataclass
class Document:
    filename: str
    content: str

    def __post_init__(self):
        if not isinstance(self.filename, str):
            raise TypeError("str")
        pattern = r"^[a-zA-Z0-9]+\.json$"
        if not re.match(pattern, self.filename):
            raise TypeError("Введите валидное название файла *.json")
        