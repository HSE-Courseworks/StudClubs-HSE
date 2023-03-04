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
    await rename_event.R1.set()

@dp.message_handler(state=rename_event.R1)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(R1=answer)
    data = await state.get_data()
    Name_event = data.get('R1')
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
    await rename_event.R2.set()

@dp.message_handler(state=rename_event.R2)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(R2=answer)
    data = await state.get_data()
    if data.get('R2').lower() == 'да':
        await message.answer('Мероприятие успешно добавлено в БД')
        await state.finish()
    elif data.get('R2').lower() == 'нет':
        await state.finish()
        await message.answer('что бы вы хотели изменить?', reply_markup=ikb_menu)



@dp.callback_query_handler(text='описание')
async def send_message(call: CallbackQuery):
    await call.message.answer('Введите новое описание')
    await rename_event.R3.set()

@dp.message_handler(state=rename_event.R3)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(R3=answer)
    data = await state.get_data()
    description_event = data.get('R3')
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
    await rename_event.R2.set()
@dp.callback_query_handler(text='ссылка')
async def send_message(call: CallbackQuery):
    await call.message.answer('Введите новую ссылку')
    await rename_event.R4.set()

@dp.message_handler(state=rename_event.R4)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(R4=answer)
    data = await state.get_data()
    link_event = data.get('R4')
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
    await rename_event.R2.set()

@dp.callback_query_handler(text='дата')
async def send_message(call: CallbackQuery):
    await call.message.answer('Введите новую дату')
    await rename_event.R5.set()

@dp.message_handler(state=rename_event.R5)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(R5=answer)
    data = await state.get_data()
    date_event = data.get('R5')
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
    await rename_event.R2.set()
@dp.callback_query_handler(text='время')
async def send_message(call: CallbackQuery):
    await call.message.answer('Введите новое время')
    await rename_event.R6.set()

@dp.message_handler(state=rename_event.R6)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(R6=answer)
    data = await state.get_data()
    time_event = data.get('R6')
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
    await rename_event.R2.set()

@dp.callback_query_handler(text='место')
async def send_message(call: CallbackQuery):
    await call.message.answer('Введите новое место')
    await rename_event.R7.set()

@dp.message_handler(state=rename_event.R7)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(R7=answer)
    data = await state.get_data()
    place_event = data.get('R7')
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
    await rename_event.R2.set()
