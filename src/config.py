#Не добавлять свои данные в Git
from urllib.parse import urlencode #Парсит query-параметры

#Заменить на свое
school_domain = ""
login = ""
password = ""

#Advanced
chunk_size = 500

#Автоопределяющееся
eljur_url = f"https://{school_domain}.eljur.ru"
auth_site_url = eljur_url + "/authorize"
ajax_auth_url = eljur_url + "/ajaxauthorize"
messages_url = eljur_url + "/journal-messages-action"
sent_messages_url = messages_url + "/category.sent"
api_messages_url = eljur_url + "/journal-api-messages-action"
user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"


eljur_homepage_params = {
    "user" : login,
    "domain" : school_domain
}

#Использовать только в config.py!
homepage_with_params = f"{eljur_url}/?{urlencode(eljur_homepage_params)}"
"""
Используется только в "referer" поле, заголовка.
"""

#Заголовки
#Content-Length: мимо, считается request'ом (urllib3)
#Content-Type: пускай сам считает
#Accept-Encoding: gzip и deflate «из коробки», br с "brotlicffi", zstd - нет.

ajax_auth_headers = { #Откуда-то он берет ej_fonts куки
    "accept" : "*/*",
    "accept-encoding" : "gzip, deflate, br",
    "accept-language" : "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "dnt" : "1",
    "origin" : eljur_url,
    "priority" : "u=1, i",
    "referer" : auth_site_url,
    "sec-ch-ua" : '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    "sec-ch-ua-mobile" : "?0",
    "sec-ch-ua-platform" : "Windows",
    "sec-fetch-dest" : "empty",
    "sec-fetch-mode" : "cors",
    "sec-fetch-site" : "same-origin",
    "sec-gpc" : "1",
    "upgrade-insecure-requests" : "1",
    "user-agent" : user
}

homepage_headers = {
    "accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding" : "gzip, deflate, br",
    "accept-language" : "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "dnt" : "1",
    "priority" : "u=0, i",
    "referer": auth_site_url,
    "sec-ch-ua" : '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    "sec-ch-ua-mobile" : "?0",
    "sec-ch-ua-platform" : "Windows",
    "sec-fetch-dest" : "empty",
    "sec-fetch-mode" : "cors",
    "sec-fetch-site" : "same-origin",
    "sec-fetch-user" : "?1",
    "sec-gpc" : "1",
    "upgrade-insecure-requests" : "1",
    "user-agent": user
}

messagepage_headers = {
    **homepage_headers,
    "referer" : homepage_with_params
}
sent_messagepage_headers = {
    **messagepage_headers,
    "referer" : sent_messages_url
}
messageget_headers = {
    **ajax_auth_headers,
    "referer" : messages_url
}
messageget_headers.pop("origin", None)

sent_messageget_headers = {
    **messageget_headers,
    "referer" : sent_messages_url
}

messageget_params = {
    "method" : "messages.get_list",
    "category" : "inbox",
    "search" : "",
    "limit" : "20",
    "offset" : "0",
    "teacher" : "", #Потом откуда-то берется это значение
    "status" : "",
    "companion" : "", #Потом равен 0
    "minDate" : "0"
}
"""
Поставить после первого использования ключ teacher и companion, изменить referer (добавив category, teacher и offset
"""
#Полезная нагрузка
ajax_auth_data = {
    "username" : login,
    "password" : password,
    "return_uri" : "/"
}

def messagereferer_url_build():
    mes_params = {
        "category" : messageget_params["category"],
        "teacher" : messageget_params["teacher"],
        "offset" : messageget_params["offset"]
    }
    return f"{messages_url}?{urlencode(mes_params)}"

fileget_headers = {
    **homepage_headers,
    'sec-fetch-dest' : 'document'
}
def prefileget_headers():
    fileget_headers['referer'] = messageget_params["referer"]




