
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton


# Reply Keyboards
start_reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="👋 Register!")],
        [KeyboardButton(text="ℹ About Me")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Let's get started!",
    selective=True,
)


role_reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Adminstrator")],
        [KeyboardButton(text="User")],

    ],
    input_field_placeholder="How may I help you?",
    one_time_keyboard=True,
    selective=True,
    resize_keyboard=True,

)