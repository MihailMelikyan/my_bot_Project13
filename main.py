from aiogram import Bot, Dispatcher, executor, types
import asyncio
from aiogram.contrib.fsm_storage.memory import MemoryStorage

api = "7593311120:AAFOUY74rQnQEc1wmNsFzXY-It4KKQbsPvE"
bot = Bot(token=api)
dp = Dispatcher(bot, storage= MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler()
async def all_message(message):
    print('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
