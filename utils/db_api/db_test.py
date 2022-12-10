import asyncio

from data import config
from utils.db_api.db_gino import db
from utils.db_api import quick_commands as commands
async def db_test():
    await db.set_bind(config.POSTGRES_URI)
    await db.gino.drop_all()
    await db.gino.create_all()

    await commands.add_user(1, "Влад", 'net')
    await commands.add_user(1124, "В23423лад", 'какое-то имя')
    await commands.add_user(1123, "Влавапвард", 'sdffs')
    await commands.add_user(9, "Влвыффвад", 'd4')

    users = await commands.select_all_users()
    print(users)

    count = await commands.count_users()
    print(count)

    user = await commands.select_user(1)
    print(user)

    await commands.update_user_name(1, "новое Влад имя")
    print(user)

loop = asyncio.get_event_loop()
loop.run_until_complete(db_test())
