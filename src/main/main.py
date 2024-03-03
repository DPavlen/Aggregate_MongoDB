import asyncio
from dotenv import load_dotenv
import logging
import os
import pymongo

from aiogram import Bot, Dispatcher, types

from src.handlers.handlers import router
from src.handlers import aggregate_month

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
dp = Dispatcher()


dp.message_handler(lambda message: message.text == "Агрегация по месяцу", aggregate_month)
async def handle_aggregate_month(message: types.Message):
    # Ваш код обработки для агрегации по месяцу
    await message.answer("Вы выбрали агрегацию по месяцу")


async def main() -> None:
    """Основная логика для запуска."""
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=BOT_TOKEN)
    dp.include_router(router)
    dp.register_message_handler(handle_aggregate_month,
                                lambda message: message.text == "Агрегация по месяцу",
                                reply_markup=main)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
