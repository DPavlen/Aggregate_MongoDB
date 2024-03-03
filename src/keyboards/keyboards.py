from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Создаем клавиатуру и потом добавляем в нее кнопки
main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Агрегация по месяцу")],
    [KeyboardButton(text="Агрегация по дню")],
    [KeyboardButton(text="Агрегация по часу")],
],
    resize_keyboard=True,
    input_field_placeholder="Выберите пункт меню!",
)
