import random
import time

import const

def wait_time_for_req():
    time.sleep(random.uniform(0.5, 1.3))

def wait_time_for_file_download():
    time.sleep(random.uniform(0.1, 0.2))

def calc_halfyear(month):
    if 1 <= int(month) <= 6:
        return "1"
    return "2"


def create_rec_message_folder(msg_date, sender_name):
    ye_mo_da = msg_date.split()[0].split("-")  # ['2025', '06', '23']
    halfyear = f"{ye_mo_da[0]}_{calc_halfyear(ye_mo_da[1])}"
    mo_da = f"{ye_mo_da[1]}.{ye_mo_da[2]}"

    base_dir = const.ELJUR_RECEIVED_DATA_DIR / halfyear / sender_name / mo_da

    # Ищем первый свободный номер папки
    num = 1
    while (base_dir / str(num)).exists():
        num += 1

    message_dir = base_dir / str(num)
    message_dir.mkdir(parents=True, exist_ok=True)
    return message_dir

def create_sent_message_folder(msg_date, sender_name):
    ye_mo_da = msg_date.split()[0].split("-")  # ['2025', '06', '23']
    halfyear = f"{ye_mo_da[0]}_{calc_halfyear(ye_mo_da[1])}"
    mo_da = f"{ye_mo_da[1]}.{ye_mo_da[2]}"

    base_dir = const.ELJUR_SENT_DATA_DIR / halfyear / sender_name / mo_da

    # Ищем первый свободный номер папки
    num = 1
    while (base_dir / str(num)).exists():
        num += 1

    message_dir = base_dir / str(num)
    message_dir.mkdir(parents=True, exist_ok=True)
    return message_dir

def create_file_path(message_folder, filename):
    path_to_file = message_folder  / filename
    path_to_file.parent.mkdir(parents=True, exist_ok=True)
    return path_to_file

def write_into_file(filepath, text):
    with open(filepath, 'w', encoding="utf-8") as f:
        f.write(text)


def write_msg_data(path_to_message, subject, msg_text, msg_date):
    path_for_msg_data = path_to_message / "msg_data"
    path_for_msg_data.mkdir(parents=True, exist_ok=True)
    #path to message/msg_data/
    write_into_file(path_for_msg_data / "subject.txt", subject)
    write_into_file(path_for_msg_data / "msg_text.txt", msg_text)
    write_into_file(path_for_msg_data / "msg_date.txt", msg_date)

