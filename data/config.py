import os # os - библиотека функций для работы с операционной системой

from dotenv import load_dotenv # Импортируем функцию load_dotenv

load_dotenv() # Запускаем функцию которая загружает переменное окружение из фала .env

#получаем токен бота
BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

# список администраторов бота
admins = [
    710349061
]
