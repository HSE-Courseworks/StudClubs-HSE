from aiogram.dispatcher.filters import Command
from aiogram import types
from loader import dp
from states import reg_admin
from states import reg_yes_no_admin
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from keyboards.inline import choice_admin_position
from keyboards.inline import rechoice_admin_position
from loader import bot
from keyboards.inline import yes_no_new_admin
from keyboards.inline import edit_regisration_admin

from utils.db_api import quick_commands as commands

flag = True
info = []
"""
await commands.add_admin(admin_id=message.from_user.id,
                             first_name=message.from_user.first_name,
                             last_name=message.from_user.last_name,
                             username=message.from_user.username,
                             position='adm',
                             club_id=0 #0 значит что может редачть мероприятия всех клубов
                             )
"""
@dp.message_handler(Command('serafim_admin'))
async def new_admin_(message: types.Message):
    if message.from_user.id == 710349061:
        await commands.add_admin(admin_id=message.from_user.id,
                                 first_name=message.from_user.first_name,
                                 last_name=message.from_user.last_name,
                                 username=message.from_user.username,
                                 FIO='Кравчук Серафим Павлович',
                                 vk_link='https://vk.com/batkovich001',
                                 position='org',
                                 club_id=0)
        await message.answer('Это успех')

@dp.message_handler(Command('new_admin'))
async def new_admin_(message: types.Message):
    await message.answer('Привет, ты начал регистрацию чтоб стать администратором или организатором.\n\nНапиши своё ФИО:')
    await reg_admin.fio_admin.set()

@dp.message_handler(state=reg_admin.fio_admin)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(admin_id=message.from_user.id)
    await state.update_data(first_name=message.from_user.first_name)
    await state.update_data(last_name=message.from_user.last_name)
    await state.update_data(username=message.from_user.username)
    await state.update_data(fio_admin=answer)
    await message.answer('Напиши cсылку на свой профиль в ВК:')
    await reg_admin.vk_link_admin.set()

@dp.message_handler(state=reg_admin.vk_link_admin)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    if answer[0:15] == 'https://vk.com/':
        await state.update_data(vk_link_admin=answer)
        await state.reset_state(with_data=False)
        await message.answer('Выберите кем вы хотите быть:', reply_markup=choice_admin_position)
    else:
        await message.answer('ОШИБКА: не корректная ссылка')
        await message.answer('Напиши cсылку на свой профиль в ВК ещё раз:')
        await reg_admin.vk_link_admin.set()



@dp.callback_query_handler(text='админ')
async def send_message(call: CallbackQuery, state: FSMContext):
    await call.message.answer('Ты выбрал позицию администратора')
    await state.update_data(admin_position='admin')
    await state.update_data(ID_club_admin=0)
    await question_new_admin(call.message, state)
    await reg_admin.answer_question_admin.set()

@dp.callback_query_handler(text='куратор')
async def send_message(call: CallbackQuery, state: FSMContext):
    await state.update_data(admin_position='curator')
    ans = ''
    for i in await commands.select_all_clubs():
        S1 = f'ID: "{i.id_club}"   Название клуба: "{i.club_name}"\n'
        ans = ans + S1
    await call.message.answer(f'Ты выбрал позицию куратора клуба\n\nВот все клубы которые существуют на данный момент:\n{ans}\n\nВведи ID клуба который ты хочешь курировать:')
    await reg_admin.ID_club_admin.set()

async def check_club_id(ID):
    for i in await commands.select_all_clubs():
        if i.id_club == ID:
            return True
    return False
@dp.message_handler(state=reg_admin.ID_club_admin)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    try:
        int(answer)
        if (await check_club_id(int(answer))) == False:
            await message.answer('ОШИБКА: клуба с таким ID не существует\nВведи ID клуба который ты хочешь курировать целым числом:')
            await reg_admin.ID_club_admin.set()
        else:
            await state.update_data(ID_club_admin=int(answer))
            await question_new_admin(message, state)
            await reg_admin.answer_question_admin.set()
    except ValueError:
        await message.answer('ОШИБКА: введено не целое число\nВведи ID клуба который ты хочешь курировать целым числом:')
        await reg_admin.ID_club_admin.set()


async def question_new_admin(message, state):
    data = await state.get_data()
    FIO = data.get('fio_admin')
    link = data.get('vk_link_admin')
    club_name = ''
    position = ''
    if data.get('ID_club_admin') == 0:
        club_name = 'вы можете курировать все клубы'
    elif data.get('ID_club_admin') != 0:
        club = await commands.select_club(data.get('ID_club_admin'))
        club_name = club.club_name
    if data.get('admin_position') == 'admin':
        position = 'администратор'
    elif data.get('admin_position') == 'curator':
        position = 'куратор клуба'
    await message.answer(f'Регистрация успешно завершена\n'
                         f'ФИО: {FIO} \n'
                         f'Ссылка на ВК: {link}\n'
                         f'Вы хотите быть на позиции: {position}\n'
                         f'Название клуба который вы хотите курировать: {club_name}\n')
    await message.answer('Всё верно?\n Ответить: да/нет/отмена')


@dp.message_handler(state=reg_admin.answer_question_admin)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer_question_admin=answer)
    data = await state.get_data()
    global flag
    if data.get('answer_question_admin').lower() == 'да':
        if flag == False:
            await message.answer('Пожалуйста попробуйте подать заявку чуть-чуть позднее, в настоящее время нельзя подать заявку на рассмотрение')
        elif flag == True:
            global info
            info.append(data.get('admin_id'))
            info.append(data.get('first_name'))
            info.append(data.get('last_name'))
            info.append(data.get('username'))
            info.append(data.get('fio_admin'))
            info.append(data.get('vk_link_admin'))
            info.append(data.get('admin_position'))
            info.append(data.get('ID_club_admin'))

            admin_id = data.get('admin_id')
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            username = data.get('username')
            FIO = data.get('fio_admin')
            link = data.get('vk_link_admin')
            club_name = ''
            position = ''
            if data.get('ID_club_admin') == 0:
                club_name = 'все клубы'
            elif data.get('ID_club_admin') != 0:
                club = await commands.select_club(data.get('ID_club_admin'))
                club_name = club.club_name
            if data.get('admin_position') == 'admin':
                position = 'администратор'
            elif data.get('admin_position') == 'curator':
                position = 'куратор клуба'
            org_id = await commands.select_org_id()
            flag = False
            answer_to_org = (f'Пользователь:\n'
                             f'ID: {admin_id}\n'
                             f'First name: {first_name}\n'
                             f'Last name: {last_name}\n'
                             f'Username: {username}\n'
                             f'Хочет стать администратором или куратором клуба.\nВот данные которые ввёл пользователь:\n'
                             f'ФИО: {FIO}\n'
                             f'Ссылка на ВК: {link}\n'
                             f'Хочет быть на позиции: {position}\n'
                             f'Хочет курировать клуб: {club_name}\n\n'
                             f'Добавить пользователя?\n\n')
            await bot.send_message(org_id, answer_to_org, reply_markup=yes_no_new_admin)
            await message.answer('Ваша заявка передана на рассмотрение.\nЯ оповещу вас о результатах, как только так сразу :)')
            await state.finish()
    elif data.get('answer_question_admin').lower() == 'нет':
        await state.reset_state(with_data=False)
        await message.answer('что бы вы хотели изменить?', reply_markup=edit_regisration_admin)
    elif data.get('answer_question_admin').lower() == 'отмена':
        await state.finish()
        await message.answer('Вы отменили форму регистрации заявки на право быть администратором или куратором клуба')

@dp.callback_query_handler(text='фио')
async def send_message(call: CallbackQuery):
    await call.message.answer('Введите новое ФИО:')
    await reg_admin.update_fio_admin.set()

@dp.message_handler(state=reg_admin.update_fio_admin)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(fio_admin=answer)
    await question_new_admin(message, state)
    await reg_admin.answer_question_admin.set()

@dp.callback_query_handler(text='ссылкавк')
async def send_message(call: CallbackQuery):
    await call.message.answer('Введите новую ссылку на ваш провиль в ВК:')
    await reg_admin.update_vk_link_admin.set()

@dp.message_handler(state=reg_admin.update_vk_link_admin)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    if answer[0:15] == 'https://vk.com/':
        await state.update_data(vk_link_admin=answer)
        await question_new_admin(message, state)
        await reg_admin.answer_question_admin.set()
    else:
        await message.answer('ОШИБКА: не корректная ссылка')
        await message.answer('Введите новую ссылку на свой профиль в ВК ещё раз:')
        await reg_admin.update_vk_link_admin.set()


@dp.callback_query_handler(text='клуб')
async def send_message(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if data.get('admin_position') != 'admin':
        ans = ''
        for i in await commands.select_all_clubs():
            S1 = f'ID: "{i.id_club}"   Название клуба: "{i.club_name}"\n'
            ans = ans + S1
        await call.message.answer(f'Вот все клубы которые существуют на данный момент:\n{ans}\n\nВведи ID клуба который ты хочешь курировать:')
        await reg_admin.update_ID_club_admin.set()
    elif data.get('admin_position') == 'admin':
        await call.message.answer('ОШИБКА: вы не можете выбрать клуб так как вы выбрали позицию администратора, а администратор может курировать все кулбы.')
        await question_new_admin(call.message, state)
        await reg_admin.answer_question_admin.set()

@dp.message_handler(state=reg_admin.update_ID_club_admin)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    try:
        int(answer)
        if (await check_club_id(int(answer))) == False:
            await message.answer('ОШИБКА: клуба с таким ID не существует\nВведи ID клуба который ты хочешь курировать целым числом:')
            await reg_admin.ID_club_admin.set()
        else:
            await state.update_data(ID_club_admin=int(answer))
            await question_new_admin(message, state)
            await reg_admin.answer_question_admin.set()
    except ValueError:
        await message.answer('ОШИБКА: введено не целое число\nВведи ID клуба который ты хочешь курировать целым числом:')
        await reg_admin.update_ID_club_admin.set()



@dp.callback_query_handler(text='позиция')
async def send_message(call: CallbackQuery):
    await call.message.answer('Выберите кем вы хотите быть:', reply_markup=rechoice_admin_position)

@dp.callback_query_handler(text='reадмин')
async def send_message(call: CallbackQuery, state: FSMContext):
    await call.message.answer('Ты выбрал позицию администратора')
    await state.update_data(admin_position='admin')
    await state.update_data(ID_club_admin=0)
    await question_new_admin(call.message, state)
    await reg_admin.answer_question_admin.set()

@dp.callback_query_handler(text='reкуратор')
async def send_message(call: CallbackQuery, state: FSMContext):
    await state.update_data(admin_position='curator')
    ans = ''
    for i in await commands.select_all_clubs():
        S1 = f'ID: "{i.id_club}"   Название клуба: "{i.club_name}"\n'
        ans = ans + S1
    await call.message.answer(f'Ты выбрал позицию куратора клуба\n\nВот все клубы которые существуют на данный момент:\n{ans}\n\nВведи ID клуба который ты хочешь курировать:')
    await reg_admin.update_ID_club_admin.set()

@dp.callback_query_handler(text='да_new_ad')
async def send_message(call: CallbackQuery):
    await call.message.answer(f'Пользователь успешно добавлен в админку')
    global info
    await commands.add_admin(admin_id=info[0],
                             first_name=info[1],
                             last_name=info[2],
                             username=info[3],
                             FIO=info[4],
                             vk_link=info[5],
                             position=info[6],
                             club_id=info[7])
    await bot.send_message(info[0], 'Ваша заявка на администратора или куратора клуба одобрена, вы успешно добавлены в базу данных')
    info.clear()
    global flag
    flag = True
    await reg_yes_no_admin.add_admin.set()

@dp.message_handler(state=reg_yes_no_admin.add_admin)
async def state1(message: types.Message, state: FSMContext):
    await state.finish()

@dp.callback_query_handler(text='нет_new_ad')
async def send_message(call: CallbackQuery):
    await call.message.answer('Пользователь не добавлен в админку')
    global info
    await bot.send_message(info[0], 'Ваша заявка на администратора или куратора клуба отклонена')
    info.clear()
    global flag
    flag = True
    await reg_yes_no_admin.not_add_admin.set()

@dp.message_handler(state=reg_yes_no_admin.not_add_admin)
async def state1(message: types.Message, state: FSMContext):
    await state.finish()
