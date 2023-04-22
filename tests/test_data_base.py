import pytest
from aiogram import Dispatcher #не используется тестом
from loader import dp #не используется тестом
from utils.db_api.db_gino import db
from data import config

def test_fre():
    assert 2 == 2
    print(2)

def test_on_startup():
    print('Установка связи с PostgreSQL')
    db.set_bind(config.POSTGRES_URI)
    # не работает непонятно почему (когда в файле ".env" изменяю пароли то тест проходит, хотя когда проект запускаю всё падает)

def test_create_all():
    db.gino.create_all()
    #тест всегда проходит успешно но не понятно почему так


from utils.db_api import quick_commands as commands
import aiomas #не используется тестом
import asyncio # не используется тестом почему-то
from gino import Gino #не используется тестом
import gino #не используется тестом
@pytest.mark.asyncio
async def test_add_to_DB_and_get():
    test_club_name='тестовый клуб'
    await commands.new_club(test_club_name)
    ans = ''
    for i in await commands.select_all_clubs():
        if i.club_name == test_club_name:
            ans = i.club_name
    assert test_club_name == ans
    print(ans)
    #суть в том чтобы добавить кулб в таблицу клубов и посмотреть как записалось через assert
    #куча ошибок не понимаю как исправить

