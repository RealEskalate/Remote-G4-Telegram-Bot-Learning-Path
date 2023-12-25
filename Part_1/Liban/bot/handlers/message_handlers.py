from aiogram.filters import Command
from aiogram import Router, types 
from aiogram.utils.keyboard import InlineKeyboardBuilder

# from bot.config import BotConfig

message_router = Router()


@message_router.message(Command('start'))
async def start_handler(message: types.Message):
    await message.reply("Hello Welcome to Telegram Bot Development Phase By Liban")

@message_router.message(Command('help'))
async def start_handler(message: types.Message):
    await message.reply("Hello, This is a Help command\n type /start - to get started\n /quote - to get quotes of the day")


@message_router.message(Command('quote'))
async def start_handler(message: types.Message):
    await message.reply("Currently not working, It will be implemented soon :) ")