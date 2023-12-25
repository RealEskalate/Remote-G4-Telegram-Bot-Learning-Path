from aiogram.filters import Command
from aiogram import Router, types 
from aiogram.utils.keyboard import InlineKeyboardBuilder

# from bot.config import BotConfig

message_router = Router()


@message_router.message(Command('start'))
async def start_handler(message: types.Message):
    await message.answer("Hello Welcome to Telegram Bot Development Phase")

##Help Command
@message_router.message(Command('help'))
async def start_handler(message: types.Message):
    await message.answer("Hello , I'm willing to assist you if you need any help")

##Custom Command
@message_router.message(Command('a2sv'))
async def start_handler(message: types.Message):
    await message.answer("A2SV- Africa To Silicon Valley")
