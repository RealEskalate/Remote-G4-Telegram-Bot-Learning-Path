import re

from aiogram.filters import Command
from aiogram import Router, types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ContentType
from aiogram.filters import Command

from ..keyboards import keyboard
from utils.state import Form

registration_router = Router()

registered_users = {}


@registration_router.message(Command("Register"))
async def start_handler(message: Message, state: FSMContext):
    try:
        await state.set_state(Form.role)
        await message.answer(
            "Hello Welcome to our bot. What is your role? \n- Student \n- Head"
        )
    except:
        await message.answer("Some error occurred")


@registration_router.message(Command("ListUsers"))
async def list_users_handler(message: types.Message):
    try:
        if registered_users:
            response = "<b>Registered Users:</b>\n\n"
            response += "<pre>"
            response += "Name       | Role    | Phone\n"
            response += "--------------------------------\n"

            for user_id, user_data in registered_users.items():
                user_info = (
                    user_data.get("name", "Unknown"),
                    user_data.get("role", "Unknown"),
                    user_data.get("phone_number", "Unknown"),
                )
                response += f"{user_info[0][:10]:<10} | {user_info[1][:7]:<7} | {user_info[2][:10]:<10}\n"

            response += "</pre>"
            await message.answer(response)
        else:
            await message.answer("No registered users yet.")
    except Exception as e:
        print(f"Error in list_users_handler: {e}")
        await message.answer("Some error occurred while listing users.")


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
        phone_pattern = r"[0-9]{10}"

        correctFormat = re.match(phone_pattern, message.text)
        if not correctFormat:
            await message.answer(
                "try again."
            )
            return

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


@registration_router.message(Form.photo)
async def form_name(message: Message, state: FSMContext):
    try:
        if message.content_type != ContentType.PHOTO:
            await message.answer("Please upload an image.")
            return

        photo_id = message.photo[-1].file_id
        data = await state.get_data()
        await state.clear()

        registered_users[message.from_user.id] = data

        formatted_text = []

        for key, value in data.items():
            formatted_text.append(
                f"<b>{str(key).replace('_', ' ').title()}</b>:  <i>{value}</i>"
            )

        await message.answer_photo(photo_id, "\n".join(formatted_text))
    except:
        await message.answer("Some error occurred")