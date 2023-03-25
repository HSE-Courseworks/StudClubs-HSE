from aiogram.dispatcher.filters import Command
from aiogram import types
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from loader import dp
from states import new_event
from keyboards.inline import ikb_menu_first

from datetime import datetime


from utils.db_api import quick_commands as commands
@dp.message_handler(Command('new_event')) #/new_event
async def new_event_(message: types.Message, state: FSMContext):
    admin_id = message.from_user.id
    if ((await commands.select_admin_position(admin_id)) == 'org' or (await commands.select_admin_position(admin_id)) == 'admin'):  # проверка на организатора
        await message.answer('Привет, ты начал регистрацию нового мероприятия.\nНапиши ID клуба:')
        await new_event.id_club.set()
    elif (await commands.select_admin_position(admin_id) == 'curator'):
        club_id = await commands.select_curator_idclub(admin_id)
        await state.update_data(id_club=club_id)
        club = await commands.select_club(club_id)
        club_name = club.club_name
        await message.answer(f'Привет, ты начал регистрацию нового мероприятия для клуба: {club_name}.\nНапиши название мероприятия:')
        await new_event.name_event.set()
    else:
        await message.answer('Привет, ты пока не можешь добавлять новые мероприятия так, как ты не обладаешь правами на это')

async def check_club_id(ID):
    for i in await commands.select_all_clubs():
        if i.id_club == ID:
            return True
    return False
@dp.message_handler(state=new_event.id_club)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    try:
        int(answer)
        if (await check_club_id(int(answer))) == False:
            await message.answer('ОШИБКА: клуба с таким ID не существует\nВведи ID клуба целым числом:')
            await new_event.id_club.set()
        else:
            await state.update_data(id_club=answer)
            await message.answer('Напиши название мероприятия')
            await new_event.name_event.set()
    except ValueError:
        await message.answer('ОШИБКА: введено не целое число\nВведи ID клуба целым числом:')
        await new_event.id_club.set()


@dp.message_handler(state=new_event.name_event)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(name_event=answer)
    await message.answer('Напиши краткое описание мероприятия')
    await new_event.description_event.set()
#(today_date.year == prov.year and today_date.month == prov.month and today_date.day < prov.day) or (today_date.year == prov.year and today_date.month < prov.month) or (today_date.year < prov.year)
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
    await message.answer('Напиши дату мероприятия в формате "DD.MM.YYYY":')
    await new_event.date_event.set()

@dp.message_handler(state=new_event.date_event)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(date_event=answer)
    data = await state.get_data()
    try:
        prov = datetime.strptime(data.get('date_event'), "%d.%m.%Y")
        today_date = datetime.now()
        if today_date < prov:
            await message.answer('Напиши время мероприятия в формате "hh:mm"')
            await new_event.time_event.set()
        else:
            await message.answer('ОШИБКА: введите дату которая начинается с завтрашнего дня')
            await message.answer('Напиши дату мероприятия в формате "DD.MM.YYYY":')
            await new_event.date_event.set()
    except ValueError:
        await message.answer('ОШИБКА: не корректная дата')
        await message.answer('Напиши дату мероприятия в формате "DD.MM.YYYY":')
        await new_event.date_event.set()


@dp.message_handler(state=new_event.time_event)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(time_event=answer)
    data = await state.get_data()
    try:
        prov = datetime.strptime(f"{data.get('date_event')}{data.get('time_event')}", "%d.%m.%Y%H:%M")
        await message.answer('Напиши место проведения мероприятия')
        await new_event.place_event.set()
    except ValueError:
        await message.answer('ОШИБКА: не корректное время')
        await message.answer('Напиши время мероприятия в формате "hh:mm"')
        await new_event.time_event.set()


async def question(message, state):
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

@dp.message_handler(state=new_event.place_event)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(place_event=answer)
    await question(message, state)
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
        dat = datetime.strptime(f"{data.get('date_event')}{data.get('time_event')}", "%d.%m.%Y%H:%M")
        await commands.add_event(nullified='no',
                                 succeed='no',
                                 date_time_event=dat,
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
    await question(message, state)
    await new_event.answer_question.set()

@dp.callback_query_handler(text='Описание')
async def send_message(call: CallbackQuery):
    await call.message.answer('Введите новое описание')
    await new_event.update_description.set()

@dp.message_handler(state=new_event.update_description)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(description_event=answer)
    await question(message, state)
    await new_event.answer_question.set()


@dp.callback_query_handler(text='Ссылка')
async def send_message(call: CallbackQuery):
    await call.message.answer('Введите новую ссылку')
    await new_event.update_link.set()

@dp.message_handler(state=new_event.update_link)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(link_event=answer)
    await question(message, state)
    await new_event.answer_question.set()


@dp.callback_query_handler(text='Дата')
async def send_message(call: CallbackQuery):
    await call.message.answer('Введите новую дату мероприятия в формате "DD.MM.YYYY"')
    await new_event.update_date.set()

@dp.message_handler(state=new_event.update_date)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(date_event=answer)
    data = await state.get_data()
    try:
        prov = datetime.strptime(data.get('date_event'), "%d.%m.%Y")
        today_date = datetime.now()
        if today_date < prov:
            await question(message, state)
            await new_event.answer_question.set()
        else:
            await message.answer('ОШИБКА: введите дату которая начинается с завтрашнего дня')
            await message.answer('Введите новую дату мероприятия в формате "DD.MM.YYYY"')
            await new_event.update_date.set()
    except ValueError:
        await message.answer('ОШИБКА: не корректная дата')
        await message.answer('Введите новую дату мероприятия в формате "DD.MM.YYYY"')
        await new_event.update_date.set()



@dp.callback_query_handler(text='Время')
async def send_message(call: CallbackQuery):
    await call.message.answer('Введите новое время мероприятия в формате "hh:mm"')
    await new_event.update_time.set()

@dp.message_handler(state=new_event.update_time)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(time_event=answer)
    data = await state.get_data()
    try:
        prov = datetime.strptime(f"{data.get('date_event')}{data.get('time_event')}", "%d.%m.%Y%H:%M")
        await question(message, state)
        await new_event.answer_question.set()
    except ValueError:
        await message.answer('ОШИБКА: не корректное время')
        await message.answer('Введите новое время мероприятия в формате "hh:mm"')
        await new_event.update_time.set()


@dp.callback_query_handler(text='Место')
async def send_message(call: CallbackQuery):
    await call.message.answer('Введите новое место')
    await new_event.update_place.set()

@dp.message_handler(state=new_event.update_place)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(place_event=answer)
    await question(message, state)
    await new_event.answer_question.set()