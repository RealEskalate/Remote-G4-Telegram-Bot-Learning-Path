
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton


role_reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Admin")],
        [KeyboardButton(text="User")],

    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="What do you want to do?",
    selective=True,
)