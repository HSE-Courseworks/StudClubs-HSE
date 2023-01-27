from aiogram import Bot, Dispatcher, types

from data import config

#Создаём переменную бота где Bot(token='токен нашего бота')
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)


#Создаём диспетчер
dp = Dispatcher(bot)

