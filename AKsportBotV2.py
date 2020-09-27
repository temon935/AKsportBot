import os
import time

import config
import logging
import asyncio
import ParserM
import keyboard as kb
from datetime import datetime

from aiogram import Bot, Dispatcher, executor, types


# задаем уровень логов
logging.basicConfig(level=logging.INFO)

# инициализируем бота
bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def any_msg(message):
    await bot.send_message(message.chat.id, "Чего изволите?", reply_markup=kb.greet_kb)


@dp.message_handler(commands=['del'])
async def del_func(message: types.Message):
    await bot.send_message(message.from_user.id, 'Удаляю CSV файл..', reply_markup=kb.greet_kb)
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'games.csv')
    os.remove(path)
    await bot.send_message(message.from_user.id, 'Для добавления новых данных\nНажмите search', reply_markup=kb.greet_kb)


@dp.message_handler(commands=['search'])
async def main(message: types.Message):
    try:
        loop = asyncio.get_event_loop()
        loop.create_task(scan(30))

    except TimeoutError:
        await bot.send_message(894140712, 'ЯСТРЕБ СБИТ!!!11\nКОД КРАСНЫЙ!')
        await bot.send_message(894140712, 'ПОВТОРЯЮ, ЯСТРЕБ СБИТ!!!11\nКОД КРАСНЫЙ!\nКАК СЛЫШНО, ПРИЕМ!')
        time.sleep(30)
        loop = asyncio.get_event_loop()
        loop.create_task(scan(30))


async def scan(waiting_for):
    await bot.send_message(894140712, 'Начинаю сканирование\nЕсли что-то найду - дам знать.')
    while True:
        scan = ParserM.start()
        if scan:
            await bot.send_message(894140712, scan, disable_notification=True)
            break
        else:
            await asyncio.sleep(waiting_for)
# raise asyncio.TimeoutError from None
# asyncio.exceptions.TimeoutError
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
