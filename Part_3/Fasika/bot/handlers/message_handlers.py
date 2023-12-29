from aiogram.filters import Command
from aiogram import Router, types 
from aiogram.utils.keyboard import InlineKeyboardBuilder

from ..keyboards.keyboard import reply_keyboard

message_router = Router()

@message_router.message(Command('start'))
async def start_handler(message: types.Message):
    await message.answer("Hello Welcome to Telegram Bot Development Phase", reply_markup=reply_keyboard)
    
