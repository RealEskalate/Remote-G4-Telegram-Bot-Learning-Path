from aiogram.filters import Command
from aiogram import Router, types 
from aiogram.utils.keyboard import InlineKeyboardBuilder

# from bot.config import BotConfig

message_router = Router()


@message_router.message(Command('start'))
async def start_handler(message: types.Message):
<<<<<<< HEAD
    await message.reply("Hello Welcome to Telegram Bot Development Phase")
=======
    await message.answer("Hello Welcome to Telegram Bot Development Phase")
>>>>>>> 22c7d3815afa89cd7873bf48a433d1e00958ad54
