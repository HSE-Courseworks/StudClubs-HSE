from aiogram.dispatcher.filters import Command
from aiogram import types
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from loader import dp
from states import new_event
from keyboards.inline import ikb_menu_first

from utils.db_api import quick_commands as commands
@dp.message_handler(Command('new_event')) #/new_event
async def new_event_(message: types.Message):
    await message.answer('Привет, ты начал регистрацию нового мероприятия.\nНапиши ID клуба:')
    await new_event.id_club.set()

@dp.message_handler(state=new_event.id_club)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(id_club=answer)
    await message.answer('Напиши название мероприятия')
    await new_event.name_event.set()

@dp.message_handler(state=new_event.name_event)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(name_event=answer)
    await message.answer('Напиши краткое описание мероприятия')
    await new_event.description_event.set()

@dp.message_handler(state=new_event.description_event)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(description_event=answer)
    await message.answer('Напиши ссылку для регистрации на мероприятие')
    await new_event.link_event.set()

@dp.message_handler(state=new_event.link_event)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(link_event=answer)
    await message.answer('Напиши дату мероприятия')
    await new_event.date_event.set()

@dp.message_handler(state=new_event.date_event)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(date_event=answer)
    await message.answer('Напиши время мероприятия')
    await new_event.time_event.set()

@dp.message_handler(state=new_event.time_event)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(time_event=answer)
    await message.answer('Напиши место проведения мероприятия')
    await new_event.place_event.set()

@dp.message_handler(state=new_event.place_event)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(place_event=answer)
    data = await state.get_data()
    ID_clab = data.get('id_club')
    Name_event = data.get('name_event')
    Description_event = data.get('description_event')
    Link = data.get('link_event')
    Date = data.get('date_event')
    TIME = data.get('time_event')
    Place = data.get('place_event')
    await message.answer(f'Регистрация успешно завершена\n'
                         f'IDклуба: {ID_clab} \n'
                         f'Название: {Name_event}\n'
                         f'Описание: {Description_event}\n'
                         f'Ссылка на регистрацию: {Link}\n'
                         f'Дата: {Date}\n'
                         f'Время: {TIME}\n'
                         f'Место: {Place}\n')
    await message.answer('Всё верно?\n Ответить: да/нет')
    await new_event.answer_question.set()

@dp.message_handler(state=new_event.answer_question)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer_question=answer)
    data = await state.get_data()
    if data.get('answer_question').lower() == 'да':
        ID_clab = data.get('id_club')
        Name_event = data.get('name_event')
        Description_event = data.get('description_event')
        Link = data.get('link_event')
        Date = data.get('date_event')
        TIME = data.get('time_event')
        Place = data.get('place_event')
        await commands.add_event(nullified='no',
                                 succeed='no',
                                 date_event=Date,
                                 time_event=TIME,
                                 place=Place,
                                 id_clab=int(ID_clab),
                                 name_event=Name_event,
                                 description_event=Description_event,
                                 link_event=Link,
                                 user_id=message.from_user.id,
                                 first_name=message.from_user.first_name,
                                 last_name=message.from_user.last_name,
                                 username=message.from_user.username)
        await message.answer('Мероприятие успешно добавлено в БД')
        await state.finish()
    elif data.get('answer_question').lower() == 'нет':
        await state.reset_state(with_data=False)
        await message.answer('что бы вы хотели изменить?', reply_markup=ikb_menu_first)

@dp.callback_query_handler(text='Название')
async def send_message(call: CallbackQuery):
    await call.message.answer('Введите новое название')
    await new_event.update_name.set()

@dp.message_handler(state=new_event.update_name)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(name_event=answer)
    data = await state.get_data()
    ID_clab = data.get('id_club')
    Name_event = data.get('name_event')
    Description_event = data.get('description_event')
    Link = data.get('link_event')
    Date = data.get('date_event')
    TIME = data.get('time_event')
    Place = data.get('place_event')
    await message.answer(f'Регистрация успешно завершена\n'
                         f'IDклуба: {ID_clab} \n'
                         f'Название: {Name_event}\n'
                         f'Описание: {Description_event}\n'
                         f'Ссылка на регистрацию: {Link}\n'
                         f'Дата: {Date}\n'
                         f'Время: {TIME}\n'
                         f'Место: {Place}\n')
    await message.answer('Всё верно?\n Ответить: да/нет')
    await new_event.answer_question.set()

    @dp.callback_query_handler(text='Описание')
    async def send_message(call: CallbackQuery):
        await call.message.answer('Введите новое описание')
        await new_event.update_description.set()

    @dp.message_handler(state=new_event.update_description)
    async def state1(message: types.Message, state: FSMContext):
        answer = message.text
        await state.update_data(description_event=answer)
        data = await state.get_data()
        ID_clab = data.get('id_club')
        Name_event = data.get('name_event')
        Description_event = data.get('description_event')
        Link = data.get('link_event')
        Date = data.get('date_event')
        TIME = data.get('time_event')
        Place = data.get('place_event')
        await message.answer(f'Регистрация успешно завершена\n'
                             f'IDклуба: {ID_clab} \n'
                             f'Название: {Name_event}\n'
                             f'Описание: {Description_event}\n'
                             f'Ссылка на регистрацию: {Link}\n'
                             f'Дата: {Date}\n'
                             f'Время: {TIME}\n'
                             f'Место: {Place}\n')
        await message.answer('Всё верно?\n Ответить: да/нет')
        await new_event.answer_question.set()


@dp.callback_query_handler(text='Ссылка')
async def send_message(call: CallbackQuery):
    await call.message.answer('Введите новую ссылку')
    await new_event.update_link.set()

@dp.message_handler(state=new_event.update_link)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(link_event=answer)
    data = await state.get_data()
    ID_clab = data.get('id_club')
    Name_event = data.get('name_event')
    Description_event = data.get('description_event')
    Link = data.get('link_event')
    Date = data.get('date_event')
    TIME = data.get('time_event')
    Place = data.get('place_event')
    await message.answer(f'Регистрация успешно завершена\n'
                         f'IDклуба: {ID_clab} \n'
                         f'Название: {Name_event}\n'
                         f'Описание: {Description_event}\n'
                         f'Ссылка на регистрацию: {Link}\n'
                         f'Дата: {Date}\n'
                         f'Время: {TIME}\n'
                         f'Место: {Place}\n')
    await message.answer('Всё верно?\n Ответить: да/нет')
    await new_event.answer_question.set()


@dp.callback_query_handler(text='Дата')
async def send_message(call: CallbackQuery):
    await call.message.answer('Введите новую дату')
    await new_event.update_date.set()

@dp.message_handler(state=new_event.update_date)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(date_event=answer)
    data = await state.get_data()
    ID_clab = data.get('id_club')
    Name_event = data.get('name_event')
    Description_event = data.get('description_event')
    Link = data.get('link_event')
    Date = data.get('date_event')
    TIME = data.get('time_event')
    Place = data.get('place_event')
    await message.answer(f'Регистрация успешно завершена\n'
                         f'IDклуба: {ID_clab} \n'
                         f'Название: {Name_event}\n'
                         f'Описание: {Description_event}\n'
                         f'Ссылка на регистрацию: {Link}\n'
                         f'Дата: {Date}\n'
                         f'Время: {TIME}\n'
                         f'Место: {Place}\n')
    await message.answer('Всё верно?\n Ответить: да/нет')
    await new_event.answer_question.set()


@dp.callback_query_handler(text='Время')
async def send_message(call: CallbackQuery):
    await call.message.answer('Введите новое время')
    await new_event.update_time.set()

@dp.message_handler(state=new_event.update_time)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(time_event=answer)
    data = await state.get_data()
    ID_clab = data.get('id_club')
    Name_event = data.get('name_event')
    Description_event = data.get('description_event')
    Link = data.get('link_event')
    Date = data.get('date_event')
    TIME = data.get('time_event')
    Place = data.get('place_event')
    await message.answer(f'Регистрация успешно завершена\n'
                         f'IDклуба: {ID_clab} \n'
                         f'Название: {Name_event}\n'
                         f'Описание: {Description_event}\n'
                         f'Ссылка на регистрацию: {Link}\n'
                         f'Дата: {Date}\n'
                         f'Время: {TIME}\n'
                         f'Место: {Place}\n')
    await message.answer('Всё верно?\n Ответить: да/нет')
    await new_event.answer_question.set()


@dp.callback_query_handler(text='Место')
async def send_message(call: CallbackQuery):
    await call.message.answer('Введите новое место')
    await new_event.update_place.set()

@dp.message_handler(state=new_event.update_place)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(place_event=answer)
    data = await state.get_data()
    ID_clab = data.get('id_club')
    Name_event = data.get('name_event')
    Description_event = data.get('description_event')
    Link = data.get('link_event')
    Date = data.get('date_event')
    TIME = data.get('time_event')
    Place = data.get('place_event')
    await message.answer(f'Регистрация успешно завершена\n'
                         f'IDклуба: {ID_clab} \n'
                         f'Название: {Name_event}\n'
                         f'Описание: {Description_event}\n'
                         f'Ссылка на регистрацию: {Link}\n'
                         f'Дата: {Date}\n'
                         f'Время: {TIME}\n'
                         f'Место: {Place}\n')
    await message.answer('Всё верно?\n Ответить: да/нет')
    await new_event.answer_question.set()