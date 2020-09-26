from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnHello = KeyboardButton('Погнали')
greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(btnHello)