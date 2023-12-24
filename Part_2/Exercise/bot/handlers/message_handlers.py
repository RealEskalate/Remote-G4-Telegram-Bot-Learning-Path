from aiogram.filters import Command
from aiogram import Router, types 
from aiogram.utils.keyboard import InlineKeyboardBuilder

from ..keyboards import keyboard

message_router = Router()

@message_router.message(Command('start_with_reply_keyboard'))
async def start_handler(message: types.Message):
    await message.answer("Hello Welcome to Telegram Bot Development Phase", reply_markup=keyboard.first_reply_keyboard)


@message_router.message(Command('start_with_inline_keyboard'))
async def start_handler(message: types.Message):
    await message.answer("Hello Welcome to Telegram Bot Development Phase", reply_markup=keyboard.first_inline_keyboard)

@message_router.message(Command('see_callback_buttons'))
async def start_handler(message: types.Message):
    await message.answer("Hello Welcome to Telegram Bot Development Phase", reply_markup=keyboard.second_inline_keyboard)