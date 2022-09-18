import json
import os.path
from typing import Dict


class WriteContentToFile:
    def __init__(self):
        pass

    @staticmethod
    def write_dict_to_file(file_name: str, dict_var: Dict):
        with open(os.path.join("..", "main", file_name), 'w') as file:
            file.write(json.dumps(dict_var))
