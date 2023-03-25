from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

choice_admin_position = InlineKeyboardMarkup(row_width=1,
                                             #
                                             inline_keyboard=[
                                                 [
                                                     InlineKeyboardButton(text='Администратор', callback_data='админ')
                                                 ],
                                                 [
                                                     InlineKeyboardButton(text='Куратор клуба', callback_data='куратор')
                                                 ]
                                             ])



rechoice_admin_position = InlineKeyboardMarkup(row_width=1,
                                               inline_keyboard=[
                                                   [InlineKeyboardButton(text='Администратор', callback_data='reадмин')],
                                                   [InlineKeyboardButton(text='Куратор клуба', callback_data='reкуратор')]
                                               ])
