from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from utils.db_api.db_gino import db

from data import config

#Создаём переменную бота где Bot(token='токен нашего бота')
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

#Создаём хранилище в оперативной памяти для регистрации мероприятия
storage = MemoryStorage()

#Создаём диспетчер
dp = Dispatcher(bot, storage=storage)

__all__ = ['bot', 'dp', 'db']