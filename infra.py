import json 
from pathlib import Path 
 
from typing import Dict, Any 
 
class JSONManager: 
    def __init__(self, filename: str): 
        self.filename = filename 
 
    def load_data(self) -> Dict[str, Any]: 
        """ 
        Загружает данные из файла 
        """ 
        try: 
            with open(self.filename, "r", encoding='utf-8') as f: 
                return json.load(f) 
        except (FileNotFoundError, json.JSONDecodeError): 
            raise ValueError("Такого файла не существует") 
 
    def save_data(self, data: dict) -> None: 
        """ 
        Сохраняет данные в файл 
        """ 
        try: 
            with open(self.filename, "w", encoding='utf-8') as f: 
                json.dump(data, f, ensure_ascii=False, indent=4) 
        except(FileNotFoundError, json.JSONDecodeError): 
            Path(self.filename).touch() #Создать пустой файл, если его не существует 
            with open(self.filename, "w", encoding='utf-8') as f: 
                json.dump(data, f, ensure_ascii=False, indent=4)
