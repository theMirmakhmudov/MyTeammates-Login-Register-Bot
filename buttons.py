from aiogram import types

kb1 = [
    [types.KeyboardButton(text="PDP School"), types.KeyboardButton(text="PDP University")],
    [types.KeyboardButton(text="PDP Academy")],
]
button1 = types.ReplyKeyboardMarkup(keyboard=kb1, resize_keyboard=True)
