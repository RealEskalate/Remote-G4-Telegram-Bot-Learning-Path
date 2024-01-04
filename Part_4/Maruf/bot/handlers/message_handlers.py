from aiogram.filters import Command
from aiogram import Router, types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from datetime import datetime
from aiogram.fsm.context import FSMContext
from ..keyboards import keyboard
from database.services.user_services import get_users, get_user_by_id, create_user, delete_user, update_user
from utils.state import Form
message_router = Router()
import uuid
from tabulate import tabulate


@message_router.message(Command('all_users'))
async def all_users(message: types.Message):
    try:
        users = await get_users()
        new_users_list = [{key: value for key, value in item.items() if key  in ['name', 'date', 'age',]} for item in users]

        pretty_users =tabulate(new_users_list, headers="keys", tablefmt="plain")
        print(pretty_users)
        await message.answer(f"{pretty_users}")
    except Exception as e:
        await message.answer("There is no any registered user")

@message_router.message(Command('add_user'))
async def add_users(message: types.Message, state: FSMContext):
    try:
        print("Adding user...")
        await state.set_state(Form.name)    
        await message.answer("Enter user's name: ")
    except Exception as e:
        await message.answer(f"Some error occurred:\n {e}")

@message_router.message(Command('get_user_by_id'))
async def get_by_id(message: types.Message, state: FSMContext):
    try:
        await state.set_state(Form._id)
        await message.answer("What is the id of the user you are looking for?")
    except:
        await message.answer("Some error occurred")

@message_router.message(Form.name)
async def user_adder(message: types.Message, state: FSMContext):
    try:
        name = message.text
        await state.update_data(name=name)
        await state.set_state(Form.age)
        await message.answer("Please enter your age:")
    except Exception as e:
        await message.answer(f"Some error occurred, {e}")

@message_router.message(Form.age)
async def user_adder(message: types.Message, state: FSMContext):
    try:
        age = int(message.text)
        id = uuid.uuid4()
        data = await state.get_data()
        name = data["name"]
        date = str(datetime.now().date())
        await create_user(_id=str(id), name=name, date=date, age=age)
        await message.answer('done')
        await state.clear()
    except Exception as e:
        await message.answer(f"Some error occurred, {e}")

@message_router.message(Form._id)
async def retrive_user_by_id(message: types.Message, state: FSMContext):
    try:
        print("searching user...")
        user = await get_user_by_id(message.text)
        await state.clear()
        print("searching complete...")
        print(user)
        if user:
            await message.answer(f"{user['name']}\t{user['date']}\t{user['age']}")
        else:
            await message.answer("No such user")
        
    except Exception as e:
        await message.answer(f"Some error occurred {e}")

@message_router.message(Command("delete_user"))
async def delete(message: types.Message, state: FSMContext):
    try:
        print("deleting user...")
        await message.answer("enter the id of the user to be deleted")
        await state.set_state(Form.delete_id)
    except Exception as e:
        await message.answer(f"Some error occurred {e}")

@message_router.message(Form.delete_id)
async def delete_user_by_id(message: types.Message, state: FSMContext):
    try:
        await state.clear()
        await delete_user(message.text)
        print("deletion complete...")
        await message.answer("deletion completed.")
    except Exception as e:
        await message.answer(f"Some error occurred {e}")


@message_router.message(Command("update_user"))
async def delete(message: types.Message, state: FSMContext):
    try:
        print("updating user data...")
        await message.answer("enter the id of the user his/her data to be updated.")
        await state.set_state(Form.update_id)
    except Exception as e:
        await message.answer(f"Some error occurred {e}")


@message_router.message(Form.update_id)
async def delete_user_by_id(message: types.Message, state: FSMContext):
    try:
        await state.update_data(update_id=message.text)
        await state.set_state(Form.update_name)
        await message.answer("which field do you want to update",reply_markup=keyboard.inline_reply)
    except Exception as e:
        await message.answer(f"Some error occurred {e}")


@message_router.message(Form.update_age)
async def update_user_by_id(message: types.Message, state: FSMContext):
    try:
        id = await state.get_data()
        new_age = int(message.text)
        await update_user(id=str(id["update_id"]), age=new_age)
        await message.answer("updated successfuly")
        await state.clear()
    except Exception as e:
        await message.answer(f"Some error occurred {e}")

@message_router.message(Form.update_both)
async def update_user_by_id(message: types.Message, state: FSMContext):
    try:
        id = await state.get_data()
        new_age = int(message.text)
        await update_user(id=str(id["update_id"]), age=new_age)
        await message.answer("Enter new name")
        await state.set_state(Form.update_name)
    except Exception as e:
        await message.answer(f"Some error occurred {e}")

@message_router.message(Form.update_name)
async def update_user_by_id(message: types.Message, state: FSMContext):
    try:
        id = await state.get_data()
        new_name = message.text
        await update_user(id=str(id["update_id"]), name=new_name)
        await message.answer("updated successfuly")
        await state.clear()
    except Exception as e:
        await message.answer(f"Some error occurred {e}")