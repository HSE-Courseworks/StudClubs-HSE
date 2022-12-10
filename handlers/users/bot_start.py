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

"""

@dp.message_handler(text='/new_event')
async def get_ban(message: types.Message):
    await message.answer('Напиши ID клуба')
    ID_clab = message.text
    print(ID_clab)
    await message.answer('Напиши название мероприятия')
    Name_event = str(message.text)
    print(Name_event)
    await message.answer('Напиши краткое описание мероприятия')
    Description_event = str(message.text)
    print(Description_event)
    await message.answer('Напиши ссылку для регистрации на мероприятие')
    Link = str(message.text)
    print(Link)
    await message.answer('Напиши дату мероприятия')
    Date = str(message.text)
    print(Date)
    await message.answer('Напиши время мероприятия')
    TIME = str(message.text)
    print(TIME)
    await message.answer('Напиши место проведения мероприятия')
    Place = str(message.text)
    print(Place)
    await commands.add_event(event_id= 000,
                             nullified= 'no',
                             succeed= 'no',
                             date_event=Date,
                             time_event=TIME,
                             place=Place,
                             id_clab=ID_clab,
                             name_event=Name_event,
                             description_event=Description_event,
                             link_event=Link,
                             user_id=message.from_user.id,
                             first_name=message.from_user.first_name,
                             last_name=message.from_user.last_name,
                             username=message.from_user.username)
"""
