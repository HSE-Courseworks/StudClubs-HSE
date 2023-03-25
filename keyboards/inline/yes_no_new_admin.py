from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

yes_no_new_admin = InlineKeyboardMarkup(row_width=2,
                                        inline_keyboard=[
                                            [
                                                InlineKeyboardButton(text='Да', callback_data='да_new_ad')
                                            ],
                                            [
                                                InlineKeyboardButton(text='Нет', callback_data='нет_new_ad')
                                            ]
                                        ])
