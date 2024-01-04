
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton


inline_reply = InlineKeyboardMarkup(
    inline_keyboard=[
        
           [ InlineKeyboardButton(text="Name", callback_data="name"),
            InlineKeyboardButton(text="Age", callback_data="age"),
            InlineKeyboardButton(text="Both", callback_data="both")]
    ]
)