from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton, ForceReply

first_reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="👋 Register Phone", callback_data="register_phone"),
            KeyboardButton(text="📍 Register Location", callback_data="register_location"),
        ],
        [
            KeyboardButton(text="🌐 Custom Action", callback_data="custom_action"),
            KeyboardButton(text="Inline Buttons", callback_data="inline_button"),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Type here...",
    selective=True
)

first_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👋 Register Phone", callback_data="register_phone"),
            
        ],
        [
            InlineKeyboardButton(text="🌐 Custom Action", callback_data="custom_action"),
        ]
    ]
)

second_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Action 1", callback_data="action_1"),
            InlineKeyboardButton(text="Action 2", callback_data="action_2"),
        ]
    ]
)
