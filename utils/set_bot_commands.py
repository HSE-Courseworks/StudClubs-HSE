from aiogram import types

async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Запустить бота'),
        types.BotCommand('help', 'Помощь'),
        types.BotCommand('profile', 'Получить данные из БД'),
        types.BotCommand('new_event', 'Добавить мероприятие'),
        types.BotCommand('new_event_full', 'Добавить мероприятие одним сообщением')
    ])