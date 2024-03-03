from aiogram import types, F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from src.keyboards import keyboards as keyboards

router = Router()


@router.message(CommandStart())
async def handle_start(message: types.Message):
    await message.reply(text=f"Приветики, {message.from_user.full_name}!",
                        reply_markup=keyboards.main)


@router.message(Command("help"))
async def handle_help(message: types.Message):
    text = "Я бот отвечающий на агрегацию db Mongodb.\nМожно выбрать 3 запроса!"
    await message.answer(text=text)


# @router.message()
# async def echo_message(message: types.Message):
#     await message.answer(
#         text="Такого обработчика нет",
#     )
#     try:
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         await message.reply(text="Что-то такое...")
