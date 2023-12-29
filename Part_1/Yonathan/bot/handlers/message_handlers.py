from aiogram.filters import Command
from aiogram import Router, types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# from bot.config import BotConfig

message_router = Router()


@message_router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(
        "Hello! Welcome to the A2SV Telegram Bot Development Phase. \n\n"
    )


@message_router.message(Command("help"))
async def start_handler(message: types.Message):
    await message.reply(
        """
        You can control me by sending these commands:\n
        
        /start - to get started
        /share - to share your contact details with us
        """
    )

@message_router.message(Command("share"))
async def start_handler(message: types.Message):
    await message.reply(
        """
        Please share your contact details with us by clicking the button below
        """,
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Share Contact", request_contact=True)
                ]
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )


