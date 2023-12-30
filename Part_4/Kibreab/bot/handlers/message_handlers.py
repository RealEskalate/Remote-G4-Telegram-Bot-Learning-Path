from aiogram.filters import Command
from aiogram import Router, types
from aiogram.enums.chat_action import ChatAction
from aiogram.methods.send_chat_action import SendChatAction

from database.services.user_services import get_users, get_user_by_id

message_router = Router()


@message_router.message(Command("start"))
async def start(message: types.Message):
    try:
        await message.bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
        await message.answer("Hello! I am your bot. Here are some things I can do:\n"
                             "/start - Show this information\n"
                             "/get_by_id - Get user information by ID\n"
                             "/all_users - Get a list of all users\n"
                             "/add_user - Add a new user"

                             )

    except Exception as e:
        print(f"An error occurred: {e}")
        await message.answer(f"Some error occurred: {e}")


@message_router.message(Command('all_users'))
async def all_users(message: types.Message):
    try:
        users_response = await get_users()
        users_list = users_response.users
        users_formatted = "\n".join(
            [f"{user.name} - {user.phone_number}" for user in users_list])
        await message.answer(users_formatted)
    except Exception as e:
        await message.answer(f"Some error occurred: {e}")


@message_router.message(Command("get_by_id"))
async def get_by_id(message: types.Message):
    try:
        print("searching user...")
        user_id_str = message.text.strip()

        if not user_id_str.isdigit():
            await message.answer("Please provide a valid user ID (numeric value).")
            return

        user_id = int(user_id_str)
        user = await get_user_by_id(user_id)

        if user:
            user_info = f"Name: {user.name}\nPhone: {user.phone_number}"
            await message.answer(user_info)
        else:
            await message.answer("User not found.")

        print("searching complete...")
    except Exception as e:
        print(f"An error occurred: {e}")
        await message.answer(f"Some error occurred: {e}")
