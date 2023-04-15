from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

edit_regisration_admin = InlineKeyboardMarkup(row_width=1,
                                              inline_keyboard=[
                                                  [
                                                      InlineKeyboardButton(text='ФИО', callback_data='фио')
                                                  ],
                                                  [
                                                      InlineKeyboardButton(text='Ссылку на ВК', callback_data='ссылкавк')
                                                  ],
                                                  [
                                                      InlineKeyboardButton(text='Клуб', callback_data='клуб')
                                                  ],
                                                  [
                                                      InlineKeyboardButton(text='Позицию', callback_data='позиция')
                                                  ]
                                              ])
