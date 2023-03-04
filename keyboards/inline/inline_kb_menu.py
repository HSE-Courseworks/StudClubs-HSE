from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Название', callback_data='название')
                                    ],
                                    [
                                        InlineKeyboardButton(text='Описание', callback_data='описание')
                                    ],
                                    [
                                        InlineKeyboardButton(text='Ссылка на регистрацию', callback_data='ссылка')
                                    ],
                                    [
                                        InlineKeyboardButton(text='Дата', callback_data='дата')
                                    ],
                                    [
                                        InlineKeyboardButton(text='Время проведения', callback_data='время')
                                    ],
                                    [
                                        InlineKeyboardButton(text='Место проведения', callback_data='место')
                                    ]
                                ])