import asyncio
import logging
import os
import pymongo

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from dotenv import load_dotenv

# import handlers

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

# bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(text=f"Приветики, {message.from_user.full_name}!")


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
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
