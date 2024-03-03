import asyncio
import logging
import os
import pymongo

from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from config import Config
# import handlers
from logger import logger

load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


async def main() -> None:
    """Основная логика для запуска."""
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())