
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton

type_request_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        
           [ InlineKeyboardButton(text="Pant", callback_data="pant"),
            InlineKeyboardButton(text="Shirt", callback_data="shirt")]
    ]
)

first_reply_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        
           [ InlineKeyboardButton(text="👋 Register!", callback_data="register"),
            InlineKeyboardButton(text="Explore our shop", callback_data="explore")]
    ]
)
