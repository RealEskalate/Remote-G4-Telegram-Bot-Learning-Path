from aiogram.filters import Command
from aiogram import Router, types
from aiogram.utils.keyboard import InlineKeyboardBuilder

# from bot.config import BotConfig

message_router = Router()


@message_router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.reply("Hello Welcome to Telegram Bot Development Phase.")


@message_router.message(Command("help"))
async def help_handler(message: types.Message):
    help_message = (
        "Welcome to the help section!\n"
        "Here are some commands you can use:\n"
        "/start - Start the bot\n"
        "/help - Display this help message\n"
        "/info - Get information about the bot"
    )
    await message.reply(help_message)


@message_router.message(Command("info"))
async def info_handler(message: types.Message):
    info_message = (
        "You triggered the /info command!\n"
        "This bot is a simple example bot for Telegram Bot Development Phase.\n"
        "Feel free to explore and experiment with the available commands!"
    )
    await message.answer(info_message)
