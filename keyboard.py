from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

btnUpd = InlineKeyboardButton('Обновить список игр', callback_data='2')
btnStart = InlineKeyboardButton('Сканирование Live', callback_data='1')
btnStop = InlineKeyboardButton('Посмотреть список игр', callback_data='3')
greet_kb = InlineKeyboardMarkup(resize_keyboard=True, row_width=2).add(btnStart, btnUpd, btnStop)