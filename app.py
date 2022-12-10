async def on_startup(dp):

    from loader import db
    from utils.db_api.db_gino import on_startup
    print('подключение к posgresql')
    await on_startup(dp)

    #print('удаление БД')
    #await db.gino.drop_all()

    print('создание таблиц')
    await db.gino.create_all()
    print('готово')

    from utils.notify_admins import on_sartup_notify #отправляем сообщение всем администраторам о том что бот запущен
    await on_sartup_notify(dp)

    from utils.set_bot_commands import set_default_commands
    await set_default_commands(dp)

    print("Бот запущен")

if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)