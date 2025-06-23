#Seregin Sergey
#Eljur Message Parser

#Для запросов
import requests

#Вспом. код
from utils import wait_time_for_req
import config

from received_worker import get_received_messages
from sent_worker import get_sent_messages
if __name__ == '__main__':
    session = requests.Session()
    #Запрос на аутентификацию
    session.post(config.ajax_auth_url, data=config.ajax_auth_data, headers=config.ajax_auth_headers)
    wait_time_for_req()
    #Посещаем домашнюю страницу
    session.get(config.eljur_url, params=config.eljur_homepage_params, headers=config.homepage_headers)
    wait_time_for_req()
    #Посещаем страницу сообщений
    session.get(config.messages_url, headers=config.messagepage_headers)
    wait_time_for_req()
    #Делаем тестовый запрос на 20 (по умол.) сообщений
    messages = session.get(config.api_messages_url, params=config.messageget_params, headers=config.messageget_headers)
    #Проверяем что все успешно
    messages.raise_for_status()
    #Обновляем параметры запроса под полученные из тестового запроса
    messages_dict = messages.json()
    config.messageget_params["teacher"] = messages_dict["teacher"]
    config.messageget_params["companion"] = messages_dict["companion"]
    config.messageget_params["referer"] = config.messagereferer_url_build()

    #Указываем по сколько сообщений хотим брать
    config.messageget_params["limit"] = str(config.chunk_size)
    #Переменная сколько всего сообщений (Используется что бы узнать сколько раз брать по чанку)
    total_messages = int(messages_dict['total'])

    get_received_messages(session, total_messages)

    #Посещаем страницу отправленных сообщений
    session.get(config.sent_messages_url, headers=config.sent_messagepage_headers)
    #Перемещаем подготовка к отправленным сообщениям
    config.messageget_params["category"] = "sent"
    config.messageget_params["offset"] = "0"
    config.messageget_params["referer"] = config.sent_messages_url
    #Делаем тестовый запрос отправленных, что бы получить их количество
    wait_time_for_req()
    sent_messages = session.get(config.api_messages_url, params=config.messageget_params, headers=config.messageget_headers)
    #Проверяем что все успешно
    sent_messages.raise_for_status()
    sent_messages_dict = sent_messages.json()
    total_messages = sent_messages_dict['total']

    get_sent_messages(session, total_messages)

