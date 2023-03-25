from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.user import User
from utils.db_api.schemas.user import Event
from utils.db_api.schemas.user import Admins
from utils.db_api.schemas.user import Clubs
from datetime import datetime

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



async def add_event(nullified: str, succeed: str, date_time_event: datetime, date_event: str, time_event: str, place: str, id_clab: int, name_event: str, description_event: str, link_event: str, user_id: int, first_name: str, last_name: str, username: str ):
    try:
        event = Event(nullified=nullified,succeed=succeed, date_time_event=date_time_event, date_event=date_event, time_event=time_event, place=place, id_clab=id_clab, name_event=name_event, description_event=description_event, link_event=link_event, user_id=user_id, first_name=first_name, last_name=last_name, username=username )
        await event.create()#создаём запись мероприятия в таблице
    except UniqueViolationError:
        print('Мероприятие не добавлено')

async def select_event(id_event):
    event = await Event.query.where(Event.event_id == id_event).gino.first()
    return event

async def count_events():
    count = await db.func.count(Event.event_id).gino.scalar()
    return count
async def update_name_event(id_event, new_name):
    event = await select_event(id_event)
    await event.update(name_event=new_name).apply()

async def update_description_event(id_event, new_description):
    event = await select_event(id_event)
    await event.update(description_event=new_description).apply()

async def update_link_event(id_event, new_link):
    event = await select_event(id_event)
    await event.update(link_event=new_link).apply()

async def update_date_event(id_event, new_date):
    event = await select_event(id_event)
    await event.update(date_event=new_date).apply()

async def update_time_event(id_event, new_time):
    event = await select_event(id_event)
    await event.update(time_event=new_time).apply()

async def update_place_event(id_event, new_place):
    event = await select_event(id_event)
    await event.update(place=new_place).apply()


async def add_admin(admin_id: int, first_name: str, last_name: str, username: str, FIO: str, vk_link: str, position: str, club_id: int):
    try:
        admin = Admins(admin_id=admin_id, first_name=first_name, last_name=last_name, username=username, FIO=FIO, vk_link=vk_link, position=position, club_id=club_id)
        await admin.create()
    except UniqueViolationError:
        print('Администратор не добавлен')

async def new_club(club_name: str):
    try:
        club = Clubs(club_name=club_name)
        await club.create()
    except UniqueViolationError:
        print('Клуб не добавлен')


async def select_admin_position(admin_id):
    position = await Admins.select('position').where(Admins.admin_id == admin_id).gino.scalar()
    return position

async def select_curator_idclub(admin_id):
    idclub = await Admins.select('club_id').where(Admins.admin_id == admin_id).gino.scalar()
    return idclub

async def select_org_id():
    admin_id = await Admins.select('admin_id').where(Admins.position == 'org').gino.scalar()
    return admin_id

async def select_all_clubs():
    clubs = await Clubs.query.order_by(Clubs.id_club).gino.all()
    return clubs

async def select_club(id_club):
    club = await Clubs.query.where(Clubs.id_club == id_club).gino.first()
    return club

async def update_name_club(id_club, new_name):
    club = await select_club(id_club)
    await club.update(club_name=new_name).apply()

async def delete_club(id_club):
    await Clubs.delete.where(Clubs.id_club == id_club).gino.status()