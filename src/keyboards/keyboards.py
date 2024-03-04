from aiogram.types import (ReplyKeyboardMarkup,
                           KeyboardButton,
                           InlineKeyboardMarkup,
                           InlineKeyboardButton)

# # Создаем клавиатуру и потом добавляем в нее кнопки
# main = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text="Агрегация по месяцу", callback_data="month")],
#     [KeyboardButton(text="Агрегация по дню")],
#     [KeyboardButton(text="Агрегация по часу")],
# ],
#     resize_keyboard=True,
#     input_field_placeholder="Выберите пункт меню!",
# )

# Создаем клавиатуру и потом добавляем в нее кнопки
# При нажатии определяется событие клика на кнопку
menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Агрегация по месяцу", callback_data="month")],
    [InlineKeyboardButton(text="Агрегация по дню")],
    [InlineKeyboardButton(text="Агрегация по часу")],
]
)