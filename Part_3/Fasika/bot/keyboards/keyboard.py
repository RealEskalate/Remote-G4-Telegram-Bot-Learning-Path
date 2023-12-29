from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton



reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="👋 Register"),
            KeyboardButton(text="Show Profile"),
        ],
       
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    selective=True
)



