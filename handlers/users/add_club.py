from aiogram.dispatcher.filters import Command
from aiogram import types
from loader import dp
from states import name_club
from aiogram.dispatcher import FSMContext
from utils.db_api import quick_commands as commands

@dp.message_handler(Command('add_club'))
async def new_admin_(message: types.Message):
    admin_id = message.from_user.id
    if(await commands.select_admin_position(admin_id) == 'org'): #проверка на организатора
        await message.answer('Привет, ты начал регистрацию нового клуба.\n Введи название клуба:')
        await name_club.club_name.set()
    else:
        await message.answer('Привет, ты пока не можешь добавлять новые клубы так, как ты не обладаешь правами организатора')

@dp.message_handler(state=name_club.club_name)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(club_name=answer)
    data = await state.get_data()
    await commands.new_club(data.get('club_name'))
    await message.answer(f"Ты успешно зарегистрировал клуб:\n {data.get('club_name')}")
    await state.finish()


async def check_club_id(ID):
    for i in await commands.select_all_clubs():
        if i.id_club == ID:
            return True
    return False
@dp.message_handler(Command('edit_club'))
async def new_admin_(message: types.Message):
    admin_id = message.from_user.id
    if (await commands.select_admin_position(admin_id) == 'org'):
        ans=''
        for i in await commands.select_all_clubs():
            S1 = f'ID: "{i.id_club}"   Название клуба: "{i.club_name}"\n'
            ans = ans + S1
        await message.answer(f'Вот все клубы которые существуют на данный момент:\n{ans}\n\nВведите ID клуба, у которого хотите изменить название')
        await name_club.ID_edit_club_name.set()
    else:
        await message.answer('Привет, ты пока не можешь изменять название клуба так, как ты не обладаешь правами организатора')


@dp.message_handler(state=name_club.ID_edit_club_name)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    if (await check_club_id(int(answer))) == False:
        await message.answer('ОШИБКА: клуба с таким ID не существует\nВведи ID клуба который ты хочешь курировать целым числом:')
        await name_club.ID_edit_club_name.set()
    else:
        await state.update_data(ID_edit_club_name=answer)
        await message.answer('Введи новое имя клуба')
        await name_club.edit_club_name.set()

@dp.message_handler(state=name_club.edit_club_name)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(edit_club_name=answer)
    data = await state.get_data()
    IDclub = int(data.get('ID_edit_club_name'))
    new_name_club = data.get('edit_club_name')
    await commands.update_name_club(IDclub, new_name_club)
    await message.answer(f'Название клуба с ID:{IDclub} успешно изменено на: {new_name_club}')
    await state.finish()

@dp.message_handler(Command('show_clubs'))
async def new_admin_(message: types.Message):
    ans=''
    for i in await commands.select_all_clubs():
        S1 = f'ID: "{i.id_club}"   Название клуба: "{i.club_name}"\n'
        ans = ans + S1
    await message.answer(f'Вот все клубы которые существуют на данный момент:\n{ans}')

@dp.message_handler(Command('delete_club'))
async def new_admin_(message: types.Message):
    admin_id = message.from_user.id
    if(await commands.select_admin_position(admin_id) == 'org'): #проверка на организатора
        ans = ''
        for i in await commands.select_all_clubs():
            S1 = f'ID: "{i.id_club}"   Название клуба: "{i.club_name}"\n'
            ans = ans + S1
        await message.answer(f'Вот все клубы которые существуют на данный момент:\n{ans}\n\nВведи ID клуба, который хотите удалить:')
        await name_club.ID_club_delete.set()
    else:
        await message.answer('Привет, ты пока не можешь удалить клуб так, как ты не обладаешь правами организатора')

@dp.message_handler(state=name_club.ID_club_delete)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    if (await check_club_id(int(answer))) == False:
        await message.answer('ОШИБКА: клуба с таким ID не существует\nВведи ID клуба который ты хочешь курировать целым числом:')
        await name_club.ID_club_delete.set()
    else:
        await state.update_data(ID_club_delete=answer)
        data = await state.get_data()
        await commands.delete_club(int(data.get('ID_club_delete')))
        await message.answer(f"Ты успешно удалил клуб с ID:\n {data.get('ID_club_delete')}")
        await state.finish()
