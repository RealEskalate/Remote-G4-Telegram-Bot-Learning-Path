
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton


btn_menu_show_profile = KeyboardButton(text="Show-Profile")


btn_cancel = KeyboardButton(text="Cancel")
btn_register_phone = KeyboardButton(text="register_phone", request_contact=True, )
btn_register = KeyboardButton(text="Register")
btn_inline_cancel = InlineKeyboardButton(text="Cancel", callback_data="handle_cancel",)
btn_inline_show_profile = InlineKeyboardButton(text="Show Profile", callback_data="handle_show_profile",)
register_reply_keyboard = ReplyKeyboardMarkup( resize_keyboard=True, one_time_keyboard=True, keyboard=[[btn_register]])
logged_users_reply_keyboard = ReplyKeyboardMarkup( resize_keyboard=True, one_time_keyboard=True, keyboard=[[btn_menu_show_profile]])

cancel_keyboard = ReplyKeyboardMarkup(keyboard=[[btn_cancel]], resize_keyboard=True, one_time_keyboard=True)
register_phone_keyboard = ReplyKeyboardMarkup(keyboard=[[btn_register_phone]], resize_keyboard=True, one_time_keyboard=True)
cancel_inline_keyboard =InlineKeyboardMarkup(inline_keyboard=[[btn_inline_cancel]], resize_keyboard=True, one_time_keyboard=True)
show_profile_inline = InlineKeyboardMarkup(inline_keyboard=[[btn_inline_show_profile]], resize_keyboard=True, one_time_keyboard=True)



