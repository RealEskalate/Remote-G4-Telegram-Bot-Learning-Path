from aiogram.types import (
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
)

first_reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Join Us!")],
        [KeyboardButton(text="ℹ About Us")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="dtrial",
    selective=True,
)


first_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Join Us!", url="https://www.youtube.com/watch?v=iD-cFgDDuqM&ab_channel=Netflix"
            ),
            InlineKeyboardButton(text="ℹ About Us", url="https://www.youtube.com/watch?v=iD-cFgDDuqM&ab_channel=Netflix"),
        ]
    ]
)

# inline keyboard with callback
second_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Blue Rose", callback_data="blue_rose"),
            InlineKeyboardButton(text="Red Rose", callback_data="red_rose"),
        ]
    ]
)

start_reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📱Share Your Contact", request_contact=True)],
        [KeyboardButton(text="📍Share location", request_location=True)],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="What do you wanna do?",
    selective=True,
)
