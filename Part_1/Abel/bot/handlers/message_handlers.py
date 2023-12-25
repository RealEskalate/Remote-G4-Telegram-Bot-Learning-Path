from aiogram.filters import Command
from aiogram import Router, types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# from bot.config import BotConfig

message_router = Router()


@message_router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(
        "Hello Welcome to Telegram Bot Development Phase. \n\n Check /help command for more"
    )


@message_router.message(Command("help"))
async def start_handler(message: types.Message):
    await message.reply(
        """
        Ola amigo, use the following commands at will.
        
        /start - to get started
        /location - to get location info
        """
    )


@message_router.message(Command("location"))
async def location_handler(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Share Location", request_location=True)],
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Share your location",
        selective=True,
    )

    await message.reply("Please share your location:", reply_markup=keyboard)


@message_router.message()
async def handle_location(message: types.Message):
    location = message.location
    await message.reply(
        f"Received location: Latitude {location.latitude}, Longitude {location.longitude}"
    )
