import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from dotenv import find_dotenv, load_dotenv

import handlers.handlers

load_dotenv(find_dotenv())

BOT_TOKEN = getenv('BOT_TOKEN')

dp = Dispatcher()
dp.include_router(handlers.handlers.start_router)


async def main() -> None:
    """Основная логика для запуска."""
    bot = Bot(BOT_TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    # asyncio.run(main())
