import os
import time
import csv
import config
import logging
import asyncio
import ParserM
import keyboard as kb
from aiogram import Bot, Dispatcher, executor, types


# задаем уровень логов
logging.basicConfig(level=logging.INFO)

# инициализируем бота
bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def any_msg(message: types.Message):
    await bot.send_message(message.chat.id, "Чего изволите?", reply_markup=kb.greet_kb)


@dp.callback_query_handler(lambda c: c.data)
async def callback_btn1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    if callback_query.data == '1':
        await start_scan()
    elif callback_query.data == '2':
        await del_csv()
    elif callback_query.data == '3':
        await show_csv()


async def show_csv():
    with open('games.csv') as f:
        reader = csv.DictReader(f, delimiter=';')
        for row in reader:
            show = str(row['Команда 1']) + ' - ' + str(row['Команда 2']) + '\n' + \
                   str(row['Кэф 1'])[1:] + '  vs  ' + str(row['Кэф 2'])[1:] + '\n' + str(row['Время'])
            await bot.send_message(894140712, show)
        await bot.send_message(894140712, "Чего изволите?", reply_markup=kb.greet_kb)


async def del_csv():
    await bot.send_message(894140712, 'Удаляю CSV файл..')
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'games.csv')
    os.remove(path)
    await bot.send_message(894140712, 'Для добавления новых данных\nНажмите кнопку "Сканирование"',
                           reply_markup=kb.greet_kb)


async def start_scan():
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
    game_already_showed = ''
    while True:
        parser_result = ParserM.start()
        if parser_result:
            game = parser_result.split('Ф')[0]
            if game != game_already_showed:
                await bot.send_message(894140712, parser_result, disable_notification=True)
                game_already_showed = game
                await asyncio.sleep(waiting_for)

                # break
        else:
            await asyncio.sleep(waiting_for)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
