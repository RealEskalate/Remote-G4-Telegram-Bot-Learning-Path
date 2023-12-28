import re
from aiogram.filters import Command
from aiogram import types, Router
from aiogram.fsm.context import FSMContext


from ..keyboards import keyboard

message_router = Router()

@message_router.message(Command('start'))
async def start_handler(message: types.Message):
    await message.answer("Hello! Welcome to Telegram Bot Development Phase", reply_markup=keyboard.first_reply_keyboard)

@message_router.message(lambda message: message.text == "👋 Register Phone")
async def handle_register_phone(message: types.Message, state: FSMContext):
    await message.answer("📱 Please enter your phone number to register.")
    await state.set_state("waiting_for_phone")

@message_router.message(lambda message: message.text == "📍 Register Location")
async def handle_register_location(message: types.Message, state: FSMContext):
    await message.answer("📱 Please enter location to register.")
    await state.set_state("waiting_for_location")

@message_router.message(lambda message: message.text == "🌐 Custom Action")
async def handle_custom_action(message: types.Message):
    # Your logic for handling "Custom Action" button press
    await message.answer("Performing a custom action.", reply_markup=keyboard.first_reply_keyboard)

@message_router.message(lambda message: message.text == "Inline Buttons")
async def handle_inline_buttons(message: types.Message):
    # Your logic for handling "Inline Buttons" button press
    await message.answer("Opening inline buttons.", reply_markup=keyboard.first_inline_keyboard)

@message_router.message()
async def text_message_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()

    if current_state == "waiting_for_phone":
        phone_pattern = r"[0-9]{10}"

        matched = re.match(phone_pattern, message.text)
        if matched:
            phone_number = matched.group()

            await message.answer(
                f"Thank you for sharing your phone number: {phone_number}", reply_markup=keyboard.first_reply_keyboard
            )

            await state.clear()
        else:
            await message.answer(
                "It is a wrong format, can you please check and try again."
            )
    elif current_state == "waiting_for_location":

        if message.text:
            await message.answer(
                f"Thank you for sharing your location: {message.text} ", reply_markup=keyboard.first_reply_keyboard
            )


            await state.clear()
        else:
            await message.answer(
                f"please enter your location properly"
            )

        

@message_router.message(Command('start_with_reply_keyboard'))
async def start_handler(message: types.Message):
    await message.answer("Hello Welcome to Telegram Bot Development Phase", reply_markup=keyboard.first_reply_keyboard)


@message_router.message(Command('start_with_inline_keyboard'))
async def start_handler(message: types.Message):
    await message.answer("Hello Welcome to Telegram Bot Development Phase", reply_markup=keyboard.first_inline_keyboard)

@message_router.message(Command('start'))
async def start_handler(message: types.Message):
    await message.answer("Hello Welcome to Telegram Bot Development Phase", reply_markup=keyboard.second_inline_keyboard)