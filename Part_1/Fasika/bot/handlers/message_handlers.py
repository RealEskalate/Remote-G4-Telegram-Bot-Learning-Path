from aiogram.filters import Command
from aiogram import Router, types 
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton

# from bot.config import BotConfig

message_router = Router()


@message_router.message(Command('start'))
async def start_handler(message: types.Message):
    await message.answer("Hello Welcome to Telegram Bot Development Phase")

@message_router.message(Command('help'))
async def help_handler(message: types.Message):
    await message.answer("This is a help message. You can use /start, /help, and /chat commands.")


@message_router.message(Command('chat'))
async def chat_handler(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Open Chat", url="https://t.me/fasilfm"))
    await message.answer("Click the button below to open the chat:", reply_markup=keyboard)