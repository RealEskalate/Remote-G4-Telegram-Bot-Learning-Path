from aiogram.filters import Command
from aiogram import types, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ContentType
from aiogram.filters import Command
from .profile_handler import show_profile_handler
from aiogram import Router
from ..keyboards import keyboard
from utils.state import Form
from ..keyboards.reply import cancel_markup
from ..keyboards.profile import profile_markup

registration_router = Router()

@registration_router.message(lambda message: message.text == "👋 Register")
async def start_handler(message: Message, state: FSMContext):
    try:
        await state.set_state(Form.role)
        await message.answer("Hello! Welcome to registiration. What is your role?", reply_markup=keyboard.reply_keyboard)
    except Exception as e:
        await message.answer(f"Error setting state: {e}")

@registration_router.message(Form.role)
async def form_role(message: Message, state: FSMContext):
    try:
        await state.update_data(role=message.text)
        await state.set_state(Form.phone_number)
        await message.answer("Let's register your phone number", reply_markup=cancel_markup)
    except Exception as e:
        await message.answer(f"Error updating role: {e}")

@registration_router.message(Form.phone_number)
async def form_phone(message: Message, state: FSMContext):
    try:
        await state.update_data(phone_number=message.text)
        await state.set_state(Form.name)
        await message.answer("Let's register your name", reply_markup=cancel_markup)
    except Exception as e:
        await message.answer(f"Error updating phone number: {e}")

@registration_router.message(Form.name)
async def form_name(message: Message, state: FSMContext):
    try:
        await state.update_data(name=message.text)
        await state.set_state(Form.photo)
        await message.answer("Let's register your profile picture", reply_markup=cancel_markup)
    except Exception as e:
        await message.answer(f"Error updating name: {e}")

@registration_router.message(Form.photo, F.photo)
async def form_photo(message: Message, state: FSMContext):
    try:
        photo_id = message.photo[-1].file_id
        await state.update_data(photo_id=photo_id)
        data = await state.get_data()
        # await state.clear()

        formatted_text = [f"{key}: {value}" for key, value in data.items() if key != "photo_id"]

        await message.answer_photo(photo_id, "\n".join(formatted_text), reply_markup=profile_markup)
    except Exception as e:
        await message.answer(f"Error processing photo: {e}")

# Add a command to show the profile
@registration_router.message(lambda message: message.text == "Show Profile")
async def show_profile_command_handler(message: Message, state: FSMContext):
    await show_profile_handler(message, state)


