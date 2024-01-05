from aiogram.filters import Command
from aiogram import Router, types 
from aiogram.utils.keyboard import InlineKeyboardBuilder

from ..keyboards import keyboard

message_router = Router()

@message_router.message(Command('Starter'))
async def start_handler(message: types.Message):
    try:
        await message.answer("Hello Welcome to Telegram Bot Development Phase", reply_markup=keyboard.first_reply_keyboard)
    except:
        await message.answer("Some error occurred")

@message_router.message(lambda message: message.text == "ℹ Tell me more A2SV")
async def about_me_option_handler(message: types.Message):
    await message.answer("A2SV upskills students, Next?")