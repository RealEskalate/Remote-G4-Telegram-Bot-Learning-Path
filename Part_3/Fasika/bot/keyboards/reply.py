from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

cancel_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Cancel Registration", callback_data="cancel regestration"),
           
        ],
    ]
)
