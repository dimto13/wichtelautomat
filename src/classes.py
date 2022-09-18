import datetime
import os.path
from typing import List, Dict

import pywhatkit


class InputFiles:
    def __init__(self, absolute_path_to_txt_files: str, phone_number_file_name: str = "telefon.txt",
                 tool_list_file_name: str = "werkzeug.txt"):
        self.absolute_path_to_txt_files = absolute_path_to_txt_files
        self._phone_number_file_name = phone_number_file_name
        self._tool_list_file_name = tool_list_file_name

    def get_phone_number_full_path(self):
        return os.path.join(self.absolute_path_to_txt_files, self._phone_number_file_name)

    def get_tool_list_full_path(self):
        return os.path.join(self.absolute_path_to_txt_files, self._tool_list_file_name)


class DataContent:
    def __init__(self):
        self._phone_list = None
        self._tool_list = None
        self.final_dict = {}

    def set_phone_list(self, phone: List):
        self._phone_list = phone

    def set_tool_list(self, tool: List):
        self._tool_list = tool

    def verify_lists(self):
        print("### Check if each list is unique...")
        unique_phone = list(set(self._phone_list))
        unique_tool = list(set(self._tool_list))
        if len(self._phone_list) != len(unique_phone):
            print("### Obacht, ich glaub da isch Telefonnummer doppelt drin:")
        if len(self._tool_list) != unique_tool:
            print("### Obacht, beim Werkzeug hammer was mehrfach dinna:")

        print("### Check if both lists are of same length...")
        if len(self._phone_list) != len(self._tool_list):
            print("### Luag grad nochmals noch, ob beide Lischta gleich long sand")
            print(f"Telefonlischta Zeila: {len(self._phone_list)}")
            print(f"Werkzeuglischta Zeila: {len(self._tool_list)}")

    def get_phone_list(self):
        return self._phone_list

    def get_tool_list(self):
        return self._tool_list


class WhatsApp:
    def __init__(self, sender_dict: Dict, intro_text: str):
        self._sender_dict = sender_dict
        self.intro_text = ""

    def send_message_to_whatsapp(self):
        for key, value in self._sender_dict.items():
            # need to add one minute to set a time point for sending in the future
            now_date = datetime.datetime.now() + datetime.timedelta(minutes=2)
            text = self.intro_text + " " + value
            print(f"Sending: {key} -> {text} at {now_date.hour}:{now_date.minute}")
            pywhatkit.sendwhatmsg(
                phone_no=key,
                message=text,
                time_hour=now_date.hour,
                time_min=now_date.minute,
                wait_time=40)

    def do_test_send_message(self):
        now_date = datetime.datetime.now() + datetime.timedelta(minutes=1)
        text = self.intro_text + " " + "Testnachricht am " + \
               f"{str(now_date.hour)}:{str(now_date.minute)}:{str(now_date.second)}"
        pywhatkit.sendwhatmsg(
            phone_no="+491637725729",
            message=text,
            time_hour=now_date.hour,
            time_min=now_date.minute,
            wait_time=40)
