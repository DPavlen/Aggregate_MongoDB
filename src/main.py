import asyncio
from typing import Text

from dotenv import load_dotenv
import logging
import os
import pymongo

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from aiogram import BaseMiddleware
# from aiogram.dispatcher.middlewares import BaseMiddleware
import src.keyboards.keyboards as keyboards

from src.handlers.aggregate_month import router

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
dp = Dispatcher()
# # Добавляем LoggingMiddleware
# dp.middleware.setup(LoggingMiddleware())


@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(text=f"Приветики, {message.from_user.full_name}!",
                         reply_markup=keyboards.main)


@dp.message(Command("help"))
async def handle_help(message: types.Message):
    text = "Я бот отвечающий на агрегацию db Mongodb.\nМожно выбрать 3 запроса!"
    await message.answer(text=text)


@dp.message()
async def echo_message(message: types.Message):
    await message.answer(
        text="Такого обработчика нет",
    )
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text="Что-то такое...")


async def main() -> None:
    """Основная логика для запуска."""
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=BOT_TOKEN)
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
