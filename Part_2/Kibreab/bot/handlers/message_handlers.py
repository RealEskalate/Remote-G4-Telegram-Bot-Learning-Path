import phonenumbers
from phonenumbers import NumberParseException
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from ..keyboards import keyboard

message_router = Router()


@message_router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(
        "Hello! Welcome to demo bot 2",
        reply_markup=keyboard.start_reply_keyboard,
    )


@message_router.message(lambda message: message.text == "👋 Register!")
async def register_option_handler(message: types.Message, state: FSMContext):
    await state.set_state("waiting_for_phone")
    await message.answer("Please choose an action:", reply_markup=keyboard.register_reply_keyboard)
    await message.reply("Please choose an action", reply_markup=keyboard.register_inline_keyboard)


@message_router.message(lambda message: message.text == "ℹ About Me")
async def about_me_option_handler(message: types.Message):
    await message.answer("You selected 'About Me'. What would you like to do next?")


@message_router.message()
async def text_message_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()

    if current_state == "waiting_for_phone":
        try:
            phone_number = phonenumbers.parse(message.text, None)
            if phonenumbers.is_valid_number(phone_number):
                await message.answer(f"Thank you for sharing your phone number: {phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}")
                await state.reset_state()
            else:
                await message.answer("Invalid phone number format. Please enter a valid phone number.")
        except NumberParseException:
            await message.answer("Invalid phone number format. Please enter a valid phone number.")
