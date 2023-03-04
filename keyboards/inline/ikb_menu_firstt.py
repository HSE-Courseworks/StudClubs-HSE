from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu_first = InlineKeyboardMarkup(row_width=1,
                                      #
                                      inline_keyboard=[
                                          [
                                              InlineKeyboardButton(text='Нaазвание', callback_data='Название')
                                          ],
                                          [
                                              InlineKeyboardButton(text='Описание', callback_data='Описание')
                                          ],
                                          [
                                              InlineKeyboardButton(text='Ссылка на регистрацию', callback_data='Ссылка')
                                          ],
                                          [
                                              InlineKeyboardButton(text='Дата', callback_data='Дата')
                                          ],
                                          [
                                              InlineKeyboardButton(text='Время проведения', callback_data='Время')
                                          ],
                                          [
                                              InlineKeyboardButton(text='Место проведения', callback_data='Место')
                                          ]
                                      ])
