from sqlalchemy import Column, BigInteger, DateTime, String, sql

from utils.db_api.db_gino import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users'
    user_id = Column(BigInteger, primary_key=True)
    first_name = Column(String(200))
    last_name = Column(String(200))
    username = Column(String(50))
    status = Column(String(30))

    query: sql.select

class Event(TimedBaseModel):
    __tablename__ = 'events'
    event_id = Column(BigInteger, primary_key=True)
    nullified = Column(String(5))
    succeed = Column(String(5))
    date_time_event = Column(DateTime(), nullable=False)
    date_event = Column(String(50))
    time_event = Column(String(50))
    place = Column(String(200))
    id_clab = Column(BigInteger)
    name_event = Column(String(100))
    description_event = Column(String(1000))
    link_event = Column(String(200))
    user_id = Column(BigInteger)
    first_name = Column(String(100))
    last_name = Column(String(100))
    username = Column(String(50))

    query: sql.select

class Clubs(TimedBaseModel):
    __tablename__ = 'clubs'
    id_club = Column(BigInteger, primary_key=True)
    club_name = Column(String(100), nullable=False)

    query: sql.select

class Admins(TimedBaseModel):
    __tablename__ = 'admins'
    admin_id = Column(BigInteger, primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    username = Column(String(50))
    FIO = Column(String(50))
    vk_link = Column(String(100))
    position = Column(String(7), nullable=False)
    club_id = Column(BigInteger)

    query: sql.select