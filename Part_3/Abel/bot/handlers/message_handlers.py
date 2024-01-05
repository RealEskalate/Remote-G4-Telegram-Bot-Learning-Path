from aiogram.filters import Command
from aiogram import Router, types

message_router = Router()


@message_router.message(Command("start"))
async def start_handler(message: types.Message):
    try:
        await message.answer(
            """
            🙋🏾‍♂️ Hello Welcome to Telegram Bot Development Phase, here are a list of commands you can use.
            \n
            /Register
            /ListUsers
            """
        )
    except:
        await message.answer("Some error occurred")
