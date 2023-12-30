import re
from aiogram.filters import Command
from aiogram import Router, types
from aiogram.fsm.context import FSMContext

from ..keyboards import keyboard

message_router = Router()


@message_router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(
        "Hello Welcome to Telegram Bot Development Phase",
        reply_markup=keyboard.start_reply_keyboard,
    )
    await message.answer(
        "Hello! Choose an action:", reply_markup=keyboard.new_inline_keyboard
    )



@message_router.message()
async def text_message_handler(msg: types.Message, state: FSMContext):
    current_state = await state.get_state()

    if current_state == "phone":
        print(current_state)
        await msg.answer(
            f"Thank you for providing your phone number: {msg.text}")
        await state.set_state("other")

    elif current_state == "name":
        print(current_state)
        await msg.answer(
            f"Thank you for providing your name: {msg.text}")
        await state.set_state("other")