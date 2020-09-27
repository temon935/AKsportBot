from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnUpd = KeyboardButton('/del')
btnStart = KeyboardButton('/search')
greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(btnUpd, btnStart)