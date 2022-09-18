from classes import WhatsApp
from read.files import ReadDictContentFromFile

if __name__ == '__main__':
    lottery_result_dict = ReadDictContentFromFile.read_dict_content(file_name="wichtel_ergebnis.json")
    whats_app_obj = WhatsApp(sender_dict=lottery_result_dict, intro_text="")

    # send messages
    whats_app_obj.do_test_send_message()
