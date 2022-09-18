import os
import pathlib
import random

from classes import InputFiles, DataContent
from read.files import ReadTxtInputFiles
from write.write_to_file import WriteContentToFile

if __name__ == '__main__':
    # Benutzer Eingabe
    result_file_name = "wichtel_ergebnis.json"

    # ********* Ab hier Finger weg ************
    input_obj = InputFiles(absolute_path_to_txt_files=os.path.join(pathlib.Path().resolve(), "..", "input"))
    # read input files
    content_phone = ReadTxtInputFiles.read_txt_file(full_file_name_path=input_obj.get_phone_number_full_path())
    content_tool = ReadTxtInputFiles.read_txt_file(full_file_name_path=input_obj.get_tool_list_full_path())

    content_obj = DataContent()
    content_obj.set_phone_list(phone=content_phone)
    content_obj.set_tool_list(tool=content_tool)

    # verify input files
    content_obj.verify_lists()

    # start random matching
    for jj in range(random.randint(10, 20)):
        random.shuffle(content_obj.get_phone_list())
        random.shuffle(content_obj.get_tool_list())
    # put lists together
    print("### Des isch na des Ergebnis:")
    list_phone = content_obj.get_phone_list()
    list_tool = content_obj.get_tool_list()
    for jj in range(0, len(content_obj.get_phone_list())):
        print(f"{list_phone[jj]} -> {list_tool[jj]}")
        content_obj.final_dict[list_phone[jj]] = list_tool[jj]

    # write out result
    WriteContentToFile.write_dict_to_file(file_name=result_file_name, dict_var=content_obj.final_dict)

    print("### Finished")
