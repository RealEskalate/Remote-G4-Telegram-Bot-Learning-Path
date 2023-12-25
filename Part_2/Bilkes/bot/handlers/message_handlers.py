from aiogram.filters import Command
from aiogram import Router, types 
from aiogram.utils.keyboard import InlineKeyboardBuilder

from ..keyboards import keyboard

message_router = Router()

@message_router.message(Command('start'))
async def start_handler(message: types.Message):
    await message.answer("Hello Welcome Telegram Bot Development Phase", reply_markup=keyboard.first_reply_keyboard)


@message_router.message(Command('learn'))
async def start_handler(message: types.Message):
    await message.answer("Hello Welcome to Learning part", reply_markup=keyboard.learn_inline_keyboard)

@message_router.message(Command('register'))
async def start_handler(message: types.Message):
    await message.answer("Which one you want to register", reply_markup=keyboard.register_inline_keyboard)


@message_router.message()
async def check_message(message: types.Message) -> None:
    if message.text == "👋 Register!":
        await message.answer("Which one you want to register", reply_markup=keyboard.register_inline_keyboard)

    
    elif message.text == "📚 Learn":
        await message.answer("Which Course you want to pick", reply_markup=keyboard.learn_inline_keyboard)
    elif message.text == "ℹ About":
        await message.answer("This bot has been developed by B:)", )

    
    # else:
        
    #     await message.reply("Good")