from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

# ------------------- School button -----------------------#
inline_button1 = InlineKeyboardBuilder()
inline_button1.row(types.InlineKeyboardButton(text="Login", callback_data="button1"))
inline_button1.row(types.InlineKeyboardButton(text="Register", callback_data="button2"))

# ------------------- University button -----------------------#

inline_button2 = InlineKeyboardBuilder()
inline_button2.row(types.InlineKeyboardButton(text="Login", callback_data="button3"))
inline_button2.row(types.InlineKeyboardButton(text="Register", callback_data="button4"))

# ------------------- Academy button -----------------------#


inline_button3 = InlineKeyboardBuilder()
inline_button3.row(types.InlineKeyboardButton(text="Login", callback_data="button5"))
inline_button3.row(types.InlineKeyboardButton(text="Register", callback_data="button6"))

