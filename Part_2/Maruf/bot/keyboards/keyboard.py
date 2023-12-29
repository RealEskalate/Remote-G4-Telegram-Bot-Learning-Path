from aiogram.types import (
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
)



start_reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📞 Phone", request_contact=True)],
        [KeyboardButton(text="🧭 Share location", request_location=True)],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="",
    selective=True,
)

new_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📞 Phone", callback_data="phone"
            ),
            InlineKeyboardButton(text="your name: ", callback_data="name"),
        ]
    ],input_field_placeholder="enter here"
)
