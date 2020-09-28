from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

btnUpd = InlineKeyboardButton('Удалить csv', callback_data='2')
btnStart = InlineKeyboardButton('Сканирование', callback_data='1')
btnStop = InlineKeyboardButton('Стоп', callback_data='3')
greet_kb = InlineKeyboardMarkup(resize_keyboard=True, row_width=2).add(btnStart, btnUpd)
stop_kb = InlineKeyboardMarkup(resize_keyboard=True, row_width=1).add(btnStop)