from aiogram.filters import Command
from aiogram import Router, types 
from aiogram.utils.keyboard import InlineKeyboardBuilder

# from bot.config import BotConfig

message_router = Router()


@message_router.message(Command('start'))
async def start_handler(message: types.Message):
    await message.reply("Hello Welcome to Telegram Bot Development Phase")