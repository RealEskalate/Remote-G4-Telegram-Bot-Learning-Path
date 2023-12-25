from aiogram.filters import Command
from aiogram import Router, types 
from aiogram.utils.keyboard import InlineKeyboardBuilder

# from bot.config import BotConfig

message_router = Router()


@message_router.message(Command('start'))
async def start_handler(message: types.Message):
    await message.reply("Hello Welcome to A2SV Remote Part1 By Tinsae Bot")

@message_router.message(Command('help'))
async def start_handler(message: types.Message):
    await message.reply("Hello, This is a Help command\n type /start - to get started\n /chat - to start chatting")


@message_router.message(Command('chat'))
async def start_handler(message: types.Message):
    await message.reply("coming soon............ :) ")