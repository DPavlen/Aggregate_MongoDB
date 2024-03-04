from aiogram import types, F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from src.keyboards import keyboards

start_router = Router()


@start_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.reply(text=f"Приветики, {message.from_user.full_name}!",
                        reply_markup=keyboards.menu)


@start_router.message(Command("help"))
async def handle_help(message: Message) -> None:
    text = "Я бот отвечающий на агрегацию db Mongodb.\nМожно выбрать 3 запроса!"
    await message.answer(text=text)


@start_router.message()
async def echo_handler(message: types.Message) -> None:
    """
    Handler will forward receive a message back to the sender
    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


# @router.callback_query(F.data == "month")
# async def month_callback(callback: CallbackQuery, ):
#     await callback.message.edit_text("RESULT")