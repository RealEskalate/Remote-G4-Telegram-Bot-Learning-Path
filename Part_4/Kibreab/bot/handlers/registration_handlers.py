from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from datetime import datetime

from ..keyboards import keyboard
from utils.state import Form
from database.services.user_services import create_user

registration_router = Router()


@registration_router.message(Command('add_user'))
async def start_handler(message: Message, state: FSMContext):
    try:
        await state.set_state(Form.role)
        await message.answer(
            "Great choice! To get started with the registration process, "
            "please select your role from the options below:", reply_markup=keyboard.role_reply_keyboard
        )
    except:
        await message.answer("Some error occurred")


@registration_router.message(Form.role)
async def form_role(message: Message, state: FSMContext):
    try:
        await state.update_data(role=message.text)
        await state.set_state(Form.phone_number)
        await message.answer("Let's register your phone number")
    except:
        await message.answer("Some error occurred")


@registration_router.message(Form.phone_number)
async def form_phone(message: Message, state: FSMContext):
    try:
        await state.update_data(phone_number=message.text)
        await state.set_state(Form.name)
        await message.answer("Let's register your name")
    except:
        await message.answer("Some error occurred")


@registration_router.message(Form.name)
async def form_photo(message: Message, state: FSMContext):
    try:
        await state.update_data(name=message.text)
        await state.set_state(Form.photo)
        await message.answer("Let's register your profile picture")
    except:
        await message.answer("Some error occurred")


@registration_router.message(Form.photo, F.photo)
async def form_name(message: Message, state: FSMContext):
    try:
        if not message.photo:
            await message.answer("Please provide a valid photo.")
            return

        await state.update_data(photo_id=message.photo[-1].file_id)
        data = await state.get_data()

        print("Adding user...")
        await create_user(int(message.chat.id), name=data['name'], phone_number=data['phone_number'], role=data['role'], photo_id=data['photo_id'], date=datetime.now())
        print("done")

    except Exception as e:
        print(f"Error adding user: {e}")
        await message.answer("Some error occurred")
