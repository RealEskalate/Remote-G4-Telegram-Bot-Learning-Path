from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

profile_markup=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Edit Profile", callback_data="edit profile"),
            InlineKeyboardButton(text="Start", callback_data="/start"),
            
        ],
    ]
)
