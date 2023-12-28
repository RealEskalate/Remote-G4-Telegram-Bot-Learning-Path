from aiogram.filters import Command
from aiogram import Router, types

from ..keyboards import keyboard

message_router = Router()


@message_router.message(Command('start'))
async def start_handler(message: types.Message):
    try:
        await message.answer("Hello Welcome to  our bot what do you want?", reply_markup=keyboard.start_reply_keyboard)
    except:
        await message.answer("Some error occurred")


@message_router.message(lambda message: message.text == "ℹ About Me")
async def about_me_option_handler(message: types.Message):
    await message.answer("You selected 'About Me'. What would you like to do next?")
