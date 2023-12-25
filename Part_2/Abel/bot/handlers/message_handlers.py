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
    await message.reply(
        "Hello! Choose an action:", reply_markup=keyboard.new_inline_keyboard
    )


@message_router.message(Command("start_with_reply_keyboard"))
async def start_handler(message: types.Message):
    await message.answer(
        "Hello Welcome to Telegram Bot Development Phase",
        reply_markup=keyboard.first_reply_keyboard,
    )


@message_router.message(Command("start_with_inline_keyboard"))
async def start_handler(message: types.Message):
    await message.answer(
        "Hello Welcome to Telegram Bot Development Phase",
        reply_markup=keyboard.first_inline_keyboard,
    )


@message_router.message(Command("see_callback_buttons"))
async def start_handler(message: types.Message):
    await message.answer(
        "Hello Welcome to Telegram Bot Development Phase",
        reply_markup=keyboard.second_inline_keyboard,
    )


@message_router.message()
async def text_message_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()

    if current_state == "waiting_for_phone":
        phone_pattern = r"[0-9]{10}"

        matched = re.match(phone_pattern, message.text)
        if matched:
            phone_number = matched.group()

            await message.answer(
                f"Thank you for sharing your phone number: {phone_number}"
            )

            await state.clear()
        else:
            await message.answer(
                "It is a wrong format, can you please check and try again."
            )
