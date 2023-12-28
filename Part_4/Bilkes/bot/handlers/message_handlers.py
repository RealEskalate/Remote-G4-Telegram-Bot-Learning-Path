from aiogram.filters import Command
from aiogram import Router, types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from datetime import datetime

from ..keyboards import keyboard
from database.services.user_services import get_users, get_user_by_id, create_user
# from database.services.user_services import  get_user_by_id
message_router = Router()

@message_router.message(Command('start'))
async def start(message: types.Message):
    await message.answer("Hello, I am a bot that can help you to manage your tasks. To get started")
    try:
        existing_user = await get_user_by_id(int(message.chat.id))
        if existing_user:
            await message.answer("Let's continue with the provided services")
            await message.answer("/get_all_users   -> View the list of Registered User\n")
            
        else:
            await message.answer("Let's start by registering you", reply_markup=keyboard.register_reply_keyboard)
    except Exception as e:
        await message.answer(f"Some error occurred: {e}")
        

@message_router.message(Command('get_all_users'))
async def all_users(message: types.Message):
    try:
        existing_user = await get_user_by_id(int(message.chat.id))
        if existing_user:
            users = await get_users()
            print(users)
            for user in users:
                
                await message.answer_photo(user.photo_id,f"\n Name= {user.name}\nAge= {user.phone_number}\nRegistration date= {user.date}")

            
        else:
            await message.answer("First you have to registered 🙏😅", reply_markup=keyboard.register_reply_keyboard)
        # await message.answer(f"{users}")
    except Exception as e:
        await message.answer(f"Some error occurred: {e}")


@message_router.message(Command('search_user_by_id'))
async def get_by_id(message: types.Message):
    try:
        existing_user = await get_user_by_id(int(message.chat.id))
        if existing_user:
            await message.answer("What is the id of the user you are looking for?\eg, ID:XXXXXXXXX")
        else:
            await message.answer("First you have to registered 🙏😅", reply_markup=keyboard.register_reply_keyboard)   
    except:
        await message.answer("Some error occurred")

# @message_router.message()
# async def retrive_user_by_id(message: types.Message):
#     try:
#         if(message.text.startswith("ID:")):
#             print("searching user...")
#             id=message.text.split(":")[-1]
#             user = await get_user_by_id(id)
#             print("searching complete...")
#             await message.answer(f"{user}")


#     except Exception as e:
#         await message.answer(f"Some error occurred {e}")


# Same way you can update and delete users