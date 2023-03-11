from aiogram import types
from aiogram.types import CallbackQuery
from keyboards.inline import ikb_menu
from states.test import rename_event

from aiogram.dispatcher import FSMContext
from loader import dp
from utils.db_api import quick_commands as commands
id_event = commands.count_events()
@dp.message_handler(text='Инлайн меню')
async def show_inline_menu(message: types.Message):
    await message.answer('что бы вы хотели изменить?!', reply_markup=ikb_menu)

@dp.callback_query_handler(text='название')
async def send_message(call: CallbackQuery):
    await call.message.answer('Введите новsasое название')
    await rename_event.edit_name.set()

@dp.message_handler(state=rename_event.edit_name)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(edit_name=answer)
    data = await state.get_data()
    Name_event = data.get('edit_name')
    id_event = await commands.count_events()
    await commands.update_name_event(id_event, Name_event)
    event = await commands.select_event(id_event)
    await message.answer(f'IDклуба: {event.id_clab}\n'
                         f'Название: {event.name_event}\n'
                         f'Описание: {event.description_event}\n'
                         f'Ссылка на регистрацию: {event.link_event}\n'
                         f'Дата: {event.date_event}\n'
                         f'Время: {event.time_event}\n'
                         f'Место: {event.place}\n')
    await message.answer('Всё верно?\n Ответить: да/нет')
    await rename_event.e_answer_q.set()

@dp.message_handler(state=rename_event.e_answer_q)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(e_answer_q=answer)
    data = await state.get_data()
    if data.get('e_answer_q').lower() == 'да':
        await message.answer('Мероприятие успешно добавлено в БД')
        await state.finish()
    elif data.get('e_answer_q').lower() == 'нет':
        await state.finish()
        await message.answer('что бы вы хотели изменить?', reply_markup=ikb_menu)



@dp.callback_query_handler(text='описание')
async def send_message(call: CallbackQuery):
    await call.message.answer('Введите новое описание')
    await rename_event.edit_description.set()

@dp.message_handler(state=rename_event.edit_description)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(edit_description=answer)
    data = await state.get_data()
    description_event = data.get('edit_description')
    id_event = await commands.count_events()
    await commands.update_description_event(id_event, description_event)
    event = await commands.select_event(id_event)
    await message.answer(f'IDклуба: {event.id_clab}\n'
                         f'Название: {event.name_event}\n'
                         f'Описание: {event.description_event}\n'
                         f'Ссылка на регистрацию: {event.link_event}\n'
                         f'Дата: {event.date_event}\n'
                         f'Время: {event.time_event}\n'
                         f'Место: {event.place}\n')
    await message.answer('Всё верно?\n Ответить: да/нет')
    await rename_event.e_answer_q.set()
@dp.callback_query_handler(text='ссылка')
async def send_message(call: CallbackQuery):
    await call.message.answer('Введите новую ссылку')
    await rename_event.edit_link.set()

@dp.message_handler(state=rename_event.edit_link)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(edit_link=answer)
    data = await state.get_data()
    link_event = data.get('edit_link')
    id_event = await commands.count_events()
    await commands.update_link_event(id_event, link_event)
    event = await commands.select_event(id_event)
    await message.answer(f'IDклуба: {event.id_clab}\n'
                         f'Название: {event.name_event}\n'
                         f'Описание: {event.description_event}\n'
                         f'Ссылка на регистрацию: {event.link_event}\n'
                         f'Дата: {event.date_event}\n'
                         f'Время: {event.time_event}\n'
                         f'Место: {event.place}\n')
    await message.answer('Всё верно?\n Ответить: да/нет')
    await rename_event.e_answer_q.set()

@dp.callback_query_handler(text='дата')
async def send_message(call: CallbackQuery):
    await call.message.answer('Введите новую дату')
    await rename_event.edit_date.set()

@dp.message_handler(state=rename_event.edit_date)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(edit_date=answer)
    data = await state.get_data()
    date_event = data.get('edit_date')
    id_event = await commands.count_events()
    await commands.update_date_event(id_event, date_event)
    event = await commands.select_event(id_event)
    await message.answer(f'IDклуба: {event.id_clab}\n'
                         f'Название: {event.name_event}\n'
                         f'Описание: {event.description_event}\n'
                         f'Ссылка на регистрацию: {event.link_event}\n'
                         f'Дата: {event.date_event}\n'
                         f'Время: {event.time_event}\n'
                         f'Место: {event.place}\n')
    await message.answer('Всё верно?\n Ответить: да/нет')
    await rename_event.e_answer_q.set()
@dp.callback_query_handler(text='время')
async def send_message(call: CallbackQuery):
    await call.message.answer('Введите новое время')
    await rename_event.edit_time.set()

@dp.message_handler(state=rename_event.edit_time)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(edit_time=answer)
    data = await state.get_data()
    time_event = data.get('edit_time')
    id_event = await commands.count_events()
    await commands.update_time_event(id_event, time_event)
    event = await commands.select_event(id_event)
    await message.answer(f'IDклуба: {event.id_clab}\n'
                         f'Название: {event.name_event}\n'
                         f'Описание: {event.description_event}\n'
                         f'Ссылка на регистрацию: {event.link_event}\n'
                         f'Дата: {event.date_event}\n'
                         f'Время: {event.time_event}\n'
                         f'Место: {event.place}\n')
    await message.answer('Всё верно?\n Ответить: да/нет')
    await rename_event.e_answer_q.set()

@dp.callback_query_handler(text='место')
async def send_message(call: CallbackQuery):
    await call.message.answer('Введите новое место')
    await rename_event.edit_place.set()

@dp.message_handler(state=rename_event.edit_place)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(edit_place=answer)
    data = await state.get_data()
    place_event = data.get('edit_place')
    id_event = await commands.count_events()
    await commands.update_place_event(id_event, place_event)
    event = await commands.select_event(id_event)
    await message.answer(f'IDклуба: {event.id_clab}\n'
                         f'Название: {event.name_event}\n'
                         f'Описание: {event.description_event}\n'
                         f'Ссылка на регистрацию: {event.link_event}\n'
                         f'Дата: {event.date_event}\n'
                         f'Время: {event.time_event}\n'
                         f'Место: {event.place}\n')
    await message.answer('Всё верно?\n Ответить: да/нет')
    await rename_event.e_answer_q.set()
