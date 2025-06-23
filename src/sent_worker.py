from math import ceil

import requests

from utils import wait_time_for_req
import utils
import config

def get_sent_messages(session: requests.Session, total_messages) -> None:
    for _ in range(ceil(total_messages / config.chunk_size)):
        wait_time_for_req()
        #Запихнуть сюда нужные
        cur_res = session.get(config.api_messages_url, params=config.messageget_params, headers=config.messageget_headers)
        cur_res_dict = cur_res.json()
        for message in cur_res_dict["list"]:
            message_name = message["subject"]
            message_date = message["msg_date"]
            message_sender = message["recipientsHuman"].replace(" ...", '')
            message_body = message["body"]
            path_to_message = utils.create_sent_message_folder(message_date, message_sender)
            for file in message['files']: #Что если файлов нет? #Тогда цикл пропустится
                filename = file['filename']
                fileurl = file['url']
                config.prefileget_headers()
                utils.wait_time_for_file_download() #Уважаем сервер, задержкой от 0.1 до 0.2, перед скачиванием файла.

                with session.get(fileurl, headers=config.fileget_headers, stream=True) as r:
                    r.raise_for_status()
                    file_path = utils.create_file_path(path_to_message, filename)
                    with open(file_path, "wb") as f:
                        for chunk in r.iter_content(chunk_size=1024*1024): #Скачивание по 1мб
                            f.write(chunk)
            utils.write_msg_data(path_to_message, message_name, message_body, message_date)
        config.messageget_params["offset"] = str(int(config.messageget_params["offset"]) + config.chunk_size)
        config.messageget_params["referer"] = config.messagereferer_url_build()