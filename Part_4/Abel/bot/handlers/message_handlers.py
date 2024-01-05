import re

from aiogram.filters import Command
from aiogram import Router, types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from datetime import datetime
from utils.state import Form, UserSearch
from aiogram.types import Message, ContentType
from aiogram.fsm.context import FSMContext


from ..keyboards import keyboard
from database.services.user_services import (
    get_users,
    get_user_by_id,
    create_user,
    update_user,
)

message_router = Router()


@message_router.message(Command("start"))
async def start_handler(message: types.Message):
    try:
        await message.answer(
            """
            🙋🏾‍♂️List of commands you can use.
            \n
            /all_users
            /add_user
            /get_user_by_id
            """
        )
    except:
        await message.answer("Some error occurred")


@message_router.message(Command("all_users"))
async def all_users(message: types.Message):
    try:
        users = await get_users()
        await message.answer(users)
    except Exception as e:
        await message.answer(f"Some error occurred: {e}")


@message_router.message(Command("add_user"))
async def add_users(message: types.Message, state: FSMContext):
    try:
        user = await get_user_by_id(message.chat.id)

        print("+++++++++++++++++++++ ", message.chat.id, user)

        if user:
            await message.answer("You have already registered.")
            return

        print("Adding user...")

        await state.set_state(Form.role)

        await message.answer(
            "Hello Welcome to our bot. What is your role? \n- Student \n- Head"
        )
    except Exception as e:
        await message.answer(f"Some error occurred:\n {e}")


@message_router.message(Command("get_user_by_id"))
async def get_by_id(message: types.Message, state: FSMContext):
    try:
        await state.set_state(UserSearch.id)
        await message.answer("What is the id of the user you are looking for?")
    except:
        await message.answer("Some error occurred")


@message_router.message(UserSearch.id)
async def retrive_user_by_id(message: types.Message, state: FSMContext):
    try:
        print("searching user...")
        user = await get_user_by_id(int(message.chat.id))
        print("searching complete...")
        await message.answer(f"{user}")
    except Exception as e:
        await message.answer(f"Some error occurred {e}")


# Same way you can update and delete users


@message_router.message(Form.role)
async def form_role(message: Message, state: FSMContext):
    try:
        await state.update_data(role=message.text)
        await state.set_state(Form.phone_number)
        await message.answer("Let's register your phone number")
    except:
        await message.answer("Some error occurred")


@message_router.message(Form.phone_number)
async def form_phone(message: Message, state: FSMContext):
    try:
        phone_pattern = r"[0-9]{10}"

        correctFormat = re.match(phone_pattern, message.text)
        if not correctFormat:
            await message.answer(
                "❌ Wrong format, can you please check and try again. \n Phone number should have 10 digits i.e. 0909090909"
            )
            return

        await state.update_data(phone_number=message.text)
        await state.set_state(Form.name)
        await message.answer("Let's register your name")
    except:
        await message.answer("Some error occurred")


@message_router.message(Form.name)
async def final_form(message: Message, state: FSMContext):
    try:
        await state.update_data(name=message.text)

        data = await state.get_data()
        data["date"] = datetime.now()
        await state.clear()

        user = await create_user(int(message.chat.id), **data)

        formatted_text = []

        for key, value in user.items():
            formatted_text.append(
                f"<b>{str(key).replace('_', ' ').title()}</b>:  <i>{value}</i>"
            )

        userInfo = "\n".join(formatted_text)

        await message.answer(userInfo)
    except Exception as e:
        await message.answer(f"Some error occurred {e}")
