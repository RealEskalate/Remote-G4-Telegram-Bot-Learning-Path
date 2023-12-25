
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton


first_reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="👋 Register!")
        ],
        [
            KeyboardButton(text="📚 Learn")
        ],
        [
            KeyboardButton(text="ℹ About")
        ],

    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="",
    selective=True
)


learn_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Java", url="https://youtu.be/eIrMbAQSU34?si=D91O1PYRrIgnpGUk"),
            InlineKeyboardButton(text="Python", url="https://youtu.be/_uQrJ0TkZlc?si=-jubBCn_StO0Piz0")
        ],
        [
            InlineKeyboardButton(text="C++", url="https://youtu.be/ZzaPdXTrSb8?si=qPF2SiDunHUCpxG-"),
            InlineKeyboardButton(text="C#", url="https://youtu.be/gfkTfcpWqAY?si=7jolotbiGbCmKvy6")
        ]
    ]
)

# inline keyboard with callback
register_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Phone", callback_data="register_phone"),
            InlineKeyboardButton(text="Location", callback_data="register_location")
        ]
    ]
)
