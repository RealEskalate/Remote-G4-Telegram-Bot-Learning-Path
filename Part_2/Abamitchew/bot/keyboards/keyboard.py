
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton

first_reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="👋 Register!")
        ],
        [
            KeyboardButton(text="ℹ About Me")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="dtrial",
    selective=True
)


first_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👋 Register!", url="https://youtu.be/CBJiJcgmDmM"),
            InlineKeyboardButton(text="ℹ About Me", url="https://youtu.be/CBJiJcgmDmM")
        ]
    ]
)

# inline keyboard with callback
second_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="action 1", callback_data="action_1"),
            InlineKeyboardButton(text="action 2", callback_data="action_2")
        ]
    ]
)

register_buttons_reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Register phone"),
            KeyboardButton(text="Register location")
        ],
        [
            KeyboardButton(text="Custom Button 1"),
            KeyboardButton(text="Custom Button 2")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    selective=True
)

# Inline keyboard with Register phone and custom buttons
register_buttons_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Register phone", callback_data="register_phone"),
            InlineKeyboardButton(text="Custom Button 1", callback_data="custom_button_1")
        ],
        [
            InlineKeyboardButton(text="Custom Button 2", callback_data="custom_button_2")
        ]
    ]
)