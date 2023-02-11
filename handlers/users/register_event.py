from aiogram.dispatcher.filters import Command
from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from states import new_event

@dp.message_handler(Command('new_event')) #/new_event
async def new_event_(message: types.Message):
    await message.answer('Привет, ты начал регистрацию нового мероприятия.\nНапиши ID клуба:')
    await new_event.test1.set()

@dp.message_handler(state=new_event.test1)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(test1=answer)
    await message.answer('Напиши название мероприятия')
    await new_event.test2.set()

@dp.message_handler(state=new_event.test2)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(test2=answer)
    await message.answer('Напиши краткое описание мероприятия')
    await new_event.test3.set()

@dp.message_handler(state=new_event.test3)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(test3=answer)
    await message.answer('Напиши ссылку для регистрации на мероприятие')
    await new_event.test4.set()

@dp.message_handler(state=new_event.test4)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(test4=answer)
    await message.answer('Напиши дату мероприятия')
    await new_event.test5.set()

@dp.message_handler(state=new_event.test5)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(test5=answer)
    await message.answer('Напиши время мероприятия')
    await new_event.test6.set()

@dp.message_handler(state=new_event.test6)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(test6=answer)
    await message.answer('Напиши место проведения мероприятия')
    await new_event.test7.set()



@dp.message_handler(state=new_event.test7)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(test7=answer)
    data = await state.get_data()
    ID_clab = data.get('test1')
    Name_event = data.get('test2')
    Description_event = data.get('test3')
    Link = data.get('test4')
    Date = data.get('test5')
    TIME = data.get('test6')
    Place = data.get('test7')
    await message.answer(f'Регистрация успешно завершена\n'
                         f'IDклуба: {ID_clab} \n'
                         f'Название: {Name_event}\n'
                         f'Описание: {Description_event}\n'
                         f'Ссылка на регистрацию: {Link}\n'
                         f'Дата: {Date}\n'
                         f'Время: {TIME}\n'
                         f'Место: {Place}\n')
    await state.finish()