from aiogram import types
from loader import dp

from utils.db_api import quick_commands as commands

@dp.message_handler(text='/start')
async def command_start(message: types.Message):
    try:
        user = await commands.select_user(message.from_user.id)
        if user.status == 'active':
            await message.answer(f'Привет {user.first_name}\n'
                                 f'Ты уже зарегистрирован')
        elif user.status == 'baned':
            await message.answer('Ты забанен')
    except Exception:
        await commands.add_user(user_id=message.from_user.id,
                                first_name=message.from_user.first_name,
                                last_name=message.from_user.last_name,
                                username=message.from_user.username,
                                status='active')
        await message.answer('Ты успешно зарегистрирован')

@dp.message_handler(text='/ban')
async def get_ban(message: types.Message):
    await commands.update_status(user_id=message.from_user.id, status='baned')
    await message.answer('Мы тебя забанили')

@dp.message_handler(text='/unban')
async def get_unban(message: types.Message):
    await commands.update_status(user_id=message.from_user.id, status='active')
    await message.answer('Ты больше не в бане')

@dp.message_handler(text='/profile')
async def profile(message: types.Message):
    user = await commands.select_user(message.from_user.id)
    await message.answer(f'ID - {user.user_id}\n'
                         f'first_name - {user.first_name}\n'
                         f'last_name - {user.last_name}\n'
                         f'username - {user.username}\n'
                         f'status - {user.status}')

@dp.message_handler(text='/prevent')
async def prevent(message: types.Message):
    event = await commands.select_event(123)
    await message.answer(f'IDклуба: {event.id_clab}\n'
                         f'Название: {event.name_event}\n'
                         f'Описание: {event.description_event}\n'
                         f'Ссылка на регистрацию: {event.link_event}\n'
                         f'Дата: {event.date_event}\n'
                         f'Время: {event.time_event}\n'
                         f'Место: {event.place}\n')