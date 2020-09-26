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


'''@dp.message_handler(commands=['start'])
async def hello_func(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет!\nНачнем зарабатывать?', reply_markup=kb.greet_kb)'''


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
    loop = asyncio.get_event_loop()
    loop.create_task(scan(30))
    executor.start_polling(dp, skip_updates=True)

