from aiogram import Bot, Dispatcher, types

from utils.db_api.db_gino import db

from data import config

#Создаём переменную бота где Bot(token='токен нашего бота')
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

#Создаём диспетчер
dp = Dispatcher(bot)

__all__ = ['bot', 'dp', 'db']