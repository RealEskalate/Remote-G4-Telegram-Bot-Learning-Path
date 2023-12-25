from aiogram.filters import Command
from aiogram import Router, types 
from aiogram.utils.keyboard import InlineKeyboardBuilder
from .variables import programming_jokes,programming_quotes

import random
# from bot.config import BotConfig




message_router = Router()


@message_router.message(Command('start'))
async def command_start_handler(message: types.Message):
    await message.answer("Hello Welcome to Yume Bot")
    await message.answer("""/start -> Welcome to the channel\n/help -> help\n/programming_quote -> 😎\n/programming_joke  -> 😁\n/contact -> contact information 
    """)



@message_router.message(Command('help'))
async def help_handler(message: types.Message):
    await message.answer("""/start -> Welcome to the channel\n/help -> help\n/programming_quote -> 😎\n/programming_joke  -> 😁\n/contact -> contact information 
    """)



@message_router.message(Command('programming_quote'))
async def quote_handler(message: types.Message):
    await message.answer(random.choice(programming_quotes))


@message_router.message(Command('programming_joke'))
async def quote_handler(message: types.Message):
    await message.answer(random.choice(programming_jokes))

@message_router.message(Command('contact'))
async def quote_handler(message: types.Message):
    await message.answer("📬")




@message_router.message()
async def echo_handler(message: types.Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        
        await message.answer("Nice try!")




