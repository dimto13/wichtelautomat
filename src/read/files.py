import json
import pickle


class ReadTxtInputFiles:
    def __init__(self):
        pass

    @staticmethod
    def read_txt_file(full_file_name_path: str):
        with open(full_file_name_path, "r") as f:
            raw_file_content = f.read()
        return list(filter(None, raw_file_content.split("\n")))


class ReadDictContentFromFile:
    def __init__(self):
        pass

    @staticmethod
    def read_dict_content(file_name: str = "wichtel_ergebnis.json"):
        with open(file_name, 'r') as handle:
            data = json.load(handle)
        return data
