from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.user import User
from utils.db_api.schemas.user import Event

async def add_user(user_id: int, first_name: str, last_name: str, username: str, status: str ):
    try:
        user = User(user_id=user_id, first_name=first_name,last_name=last_name, username=username, status=status )
        await user.create()
    except UniqueViolationError:
        print('Пользователь не добавлен')

async def select_all_users():
    users = await User.query.gino.all()
    return users

async def count_users():
    count = await db.func.count(User.user_id).gino.scalar()
    return count

async def select_user(user_id):
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user

async def update_status(user_id, status):
    user = await select_user(user_id)
    await user.update(status=status).apply()

async def add_event(nullified: str, succeed: str, date_event: str, time_event: str, place: str, id_clab: int, name_event: str, description_event: str, link_event: str, user_id: int, first_name: str, last_name: str, username: str ):
    try:
        event = Event(nullified=nullified,succeed=succeed, date_event=date_event, time_event=time_event, place=place, id_clab=id_clab, name_event=name_event, description_event=description_event, link_event=link_event, user_id=user_id, first_name=first_name, last_name=last_name, username=username )
        await event.create()#создаём запись мероприятия в таблице
    except UniqueViolationError:
        print('Мероприятие не добавлено')

async def select_all_events():
    events = await Event.query.gino.all()
    return events

#