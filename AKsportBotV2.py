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


@dp.message_handler(commands=['update'])
async def del_func(message: types.Message):
    await bot.send_message(message.from_user.id, 'Обновляю данные..', reply_markup=kb.greet_kb)
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'games.csv')
    os.remove(path)

async def scan(waiting_for):
    await bot.send_message(894140712, 'Начинаю сканирование\nЕсли что-то найду - дам знать.')
    while True:
        await asyncio.sleep(waiting_for)
        scan = ParserM.start()
        if scan:
            await bot.send_message(894140712, scan, disable_notification=True)

# raise asyncio.TimeoutError from None
# asyncio.exceptions.TimeoutError
if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()
        loop.create_task(scan(30))
        executor.start_polling(dp, skip_updates=True)
    except TimeoutError:
        bot.send_message(894140712, 'ЯСТРЕБ СБИТ!!!11\nКОД КРАСНЫЙ!')
        bot.send_message(894140712, 'ПОВТОРЯЮ, ЯСТРЕБ СБИТ!!!11\nКОД КРАСНЫЙ!\nКАК СЛЫШНО, ПРИЕМ!')
        time.sleep(30)
        loop = asyncio.get_event_loop()
        loop.create_task(scan(30))
        executor.start_polling(dp, skip_updates=True)
