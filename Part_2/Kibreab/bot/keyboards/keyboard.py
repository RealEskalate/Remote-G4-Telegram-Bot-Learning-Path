from aiogram.types import (
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
)

# Reply Keyboards
start_reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="👋 Register!")],
        [KeyboardButton(text="ℹ About Me")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Type something...",
    selective=True,
)

register_reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Register Phone", request_contact=True)],
        [KeyboardButton(text="Share Location", request_location=True)],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="What do you want to do?",
    selective=True,
)


register_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Register phone", callback_data="register_phone"
            ),
            InlineKeyboardButton(text="Share Location",
                                 callback_data="share_location"),
        ]
    ]
)
