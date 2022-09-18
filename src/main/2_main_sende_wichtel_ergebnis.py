from classes import WhatsApp
from read.files import ReadDictContentFromFile

if __name__ == '__main__':
    # read lottery result
    lottery_result_dict = ReadDictContentFromFile.read_dict_content(file_name="wichtel_ergebnis.json")
    intro_text_for_whatsapp_message = ""

    # ********* Ab hier Finger weg ************
    whats_app_obj = WhatsApp(sender_dict=lottery_result_dict, intro_text=intro_text_for_whatsapp_message)

    # send messages
    whats_app_obj.send_message_to_whatsapp()
