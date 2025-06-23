# EljurMessageParser
## О программе
EljurMessageParser скачивает все ваши сообщения и их содержимое из Eljur!

По итогу работы программы в её папке появляется папка RESULT, содержащая структуризированные по папкам сообщения и их содержимое!

Структура:
```
RESULT -> received/sent -> год_полугодие -> отправитель/получатель -> мес.день -> номер сообщения за день -> файлы сообщения и каталог msg_data -> msg_date.txt (время отправки сообщения)/msg_text.txt (текст сообщения)/subject.txt (Название сообщения)
```
```
RESULT/
├─ received/
│  └─ 2021_2/
│     ├─ Воронин А
|     |  └─ 10.15
|     |     ├─ 1
|     |     |  ├─ msg_data
|     |     |  |  ├─ msg_date.txt
|     |     |  |  ├─ msg_text.txt
|     |     |  |  └─ subject.txt
|     |     |  └─ myfile.docx
|     |     └─ 2
|     |     |  └─ msg_data
|     |     |  |  ├─ msg_date.txt
|     |     |  |  ├─ msg_text.txt
|     |     |  |  └─ subject.txt
│     └─ Волкова В. С
|        └─ 3.29
|           └─ 1
|              └─ msg_data
|                 ├─ msg_date.txt
|                 ├─ msg_text.txt
|                 └─ subject.txt
└─ sent/
```
## Подготовка
1. Скачать uv:
``` batch
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
2. Вставить свои значения в src/config.py
```
school_domain = "" (Напр. fa)
login = ""         (Напр. FunnyJoe)
password = ""      (Напр. superhardpassword)
```
3. Открыть терминал в каталоге src/
## Запуск
Что бы запустить:
``` batch
uv run main.py
```
~3000 сообщений будут скачиваться минут 3-5 и весить ~4 ГБ (если отправлялись в основном документы).
