from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

btnUpd = InlineKeyboardButton('Удалить csv', callback_data='2')
btnStart = InlineKeyboardButton('Сканирование', callback_data='1')
btnStop = InlineKeyboardButton('Посмотреть csv', callback_data='3')
greet_kb = InlineKeyboardMarkup(resize_keyboard=True, row_width=3).add(btnStart, btnUpd, btnStop)