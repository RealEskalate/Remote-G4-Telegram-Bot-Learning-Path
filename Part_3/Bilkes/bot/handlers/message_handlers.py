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



@message_router.message(Command('start'))
async def command_start_handler(message: types.Message):
    try:
        await message.answer("Hello Welcome to Telegram Bot Development Phase")
        await message.answer("""/register ->register your self into community📃 \n/help -> help\n/contact -> contact information 
        """)
    except:
        await message.answer("Some error occurred")

@message_router.message(Command('contact'))
async def quote_handler(message: types.Message):
        await message.answer("📬")

@message_router.message(Command('help'))
async def help_handler(message: types.Message):
    try:
        await message.answer("""/start -> Welcome to the channel\n/help -> help\n/register -> register your self into community📃\n/contact -> contact information 
        """)
    except:
        await message.answer("Some error occurred")
