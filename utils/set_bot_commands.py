from aiogram import types

async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Запустить бота'),
        types.BotCommand('help', 'Помощь'),
        types.BotCommand('profile', 'Получить данные из БД'),
        types.BotCommand('new_event', 'Добавить мероприятие'),
        types.BotCommand('new_admin', 'Стать администратором клуба'),
        types.BotCommand('show_clubs', 'Показать клубы'),
        types.BotCommand('add_club', 'Добавить клуб'),
        types.BotCommand('edit_club', 'Изменить название клуба'),
        types.BotCommand('delete_club', 'Удалить клуб')
    ])
