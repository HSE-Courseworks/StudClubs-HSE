from aiogram import types
from loader import dp


@dp.message_handler(text='/help')
async def command_start(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}! \n'
                         f'Тебе нужна помощь?')