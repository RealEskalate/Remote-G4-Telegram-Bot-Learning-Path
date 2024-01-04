import uuid
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext 
from datetime import datetime
from .userFormstate import UserFormState
from ..keyboards.keyboard import commands_keyboard, ActionCallback, commands_keyboard_foruser, commands_keyboard_after_reqistration
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup

from database.services.user_services import (
    get_users,
    get_user_by_id,
    create_user,
    update_user,
    delete_user_by_id,
)



message_router = Router()
# Assuming you have already defined logged_out_keyboard

# Assuming you have already defined logged_out_keyboard
logged_out_keyboard = [['Login', 'Register']]

# ...

@message_router.message(Command("start"))
async def start(message: types.Message):
    telegram_username = message.from_user.username
    if telegram_username == "Boirhanne":
        # Admin user, show regular welcome message
        welcome_message = f"Welcome to the Bot, {telegram_username}!\n Admin Use the commands below:"
        await message.answer(welcome_message, reply_markup=commands_keyboard)
    else:
        # Non-admin user, initiate login/register process
        await message.answer(f"Welcome, {telegram_username}!\n Are you an existing user or a new user?", reply_markup=commands_keyboard_foruser)


@message_router.callback_query(ActionCallback.filter(F.command=="all_users"))
async def callback_all_users(callback_query: types.CallbackQuery):
    try:
        users = await get_users()
        await callback_query.message.answer(f"All Users:\n{users}",  reply_markup=commands_keyboard)
    except Exception as e:
        await callback_query.message.answer(f"Error: {e}",  reply_markup=commands_keyboard)





@message_router.callback_query(ActionCallback.filter(F.command=="all_users"))
async def callback_all_sellers(callback_query: types.CallbackQuery):
    try:
        sellers = await get_users()
        await callback_query.message.answer(f"All Users:\n{users}",  reply_markup=commands_keyboard)
    except Exception as e:
        await callback_query.message.answer(f"Error: {e}",  reply_markup=commands_keyboard)


@message_router.callback_query(ActionCallback.filter(F.command=="add_user"))
async def callback_add_user(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer("Enter the user name:")
    await state.set_state(UserFormState.add)

@message_router.message(UserFormState.add)
async def add_user(message: types.Message, state: FSMContext):
    try:
        new_user_id = str(uuid.uuid4())
        user = await create_user(new_user_id, name=message.text, date=datetime.now())
        await message.answer(f"User added:\n{user} with ID: {new_user_id}, Role: user",  reply_markup=commands_keyboard_after_reqistration)
    except Exception as e:
        await message.answer(f"Error: {e}",  reply_markup=commands_keyboard_foruser)
    finally:
        await state.clear()



@message_router.callback_query(ActionCallback.filter(F.command=="add_seller"))
async def callback_add_seller(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer("Enter the user name:")
    await state.set_state(UserFormState.add)

@message_router.message(UserFormState.add)
async def add_seller(message: types.Message, state: FSMContext):
    try:
        new_user_id = str(uuid.uuid4())
        user = await create_user(new_user_id, name=message.text, date=datetime.now())
        await message.answer(f"User added:\n{user} with ID: {new_user_id}, Role: seller",  reply_markup=commands_keyboard)
    except Exception as e:
        await message.answer(f"Error: {e}",  reply_markup=commands_keyboard)
    finally:
        await state.clear()








@message_router.callback_query(ActionCallback.filter(F.command=="post_products"))
async def callback_post_products(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer("Enter the Product name:")
    await callback_query.message.answer("Enter the Product image:")
    await callback_query.message.answer("Enter the Product price:")
    await callback_query.message.answer("Enter the Product describtion:")
    await callback_query.message.answer("Enter the Product quantity:")
    await state.set_state(UserFormState.add)

@message_router.message(UserFormState.add)
async def post_products(message: types.Message, state: FSMContext):
    try:
        new_product_id = str(uuid.uuid4())
        product = await create_user(new_product_id, product_name=message.text, date=datetime.now())
        await message.answer(f"User added:\n{product} with ID: {new_product_id}, Role: seller",  reply_markup=commands_keyboard)
    except Exception as e:
        await message.answer(f"Error: {e}",  reply_markup=commands_keyboard)
    finally:
        await state.clear()

















# @message_router.callback_query(ActionCallback.filter(F.command == "post_products"))
# async def callback_post_products(callback_query: types.CallbackQuery, state: FSMContext):
#     try:
#         await callback_query.message.answer("Enter the Product name:")
#         await state.set_state(UserFormState.add_name)
#     except Exception as e:
#         await callback_query.message.answer(f"Error: {e}")

# @message_router.message(state=UserFormState.add_name)
# async def post_products_name(message: types.Message, state: FSMContext):
#     try:
#         await state.update_data(product_name=message.text)
#         await message.answer("Enter the Product image:")
#         await state.set_state(UserFormState.add_image)
#     except Exception as e:
#         await message.answer(f"Error: {e}")


























@message_router.callback_query(ActionCallback.filter(F.command=="get_user_by_id"))
async def callback_get_user_by_id(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer("Enter the user ID you want to retrieve:")
    await state.set_state(UserFormState.get)

@message_router.message(UserFormState.get)
async def retrieve_user_by_id(message: types.Message):
    try:
        user_id = message.text
        user = await get_user_by_id(user_id)
        await message.answer(f"User by ID {user_id}:\n{user}",  reply_markup=commands_keyboard)
    except ValueError:
        await message.answer("Invalid user ID. Please enter a valid numeric ID.",  reply_markup=commands_keyboard)
    except Exception as e:
        await message.answer(f"Error: {e}")

@message_router.callback_query(ActionCallback.filter(F.command=="update_user"))
async def callback_update_user(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer("Enter the user ID you want to update:")
    await state.set_state(UserFormState.update)

@message_router.message(UserFormState.update)
async def update_user_message(message: types.Message, state: FSMContext):
    try:
        user_id = message.text
        await message.answer(f"Enter new data for the user ID {user_id} in the format: key1=value1, key2=value2")
        await state.update_data(user_id=user_id)
        await state.set_state("waiting to update")
        
    except ValueError:
        await message.answer("Invalid user ID. Please enter a valid numeric ID.",  reply_markup=commands_keyboard)
        await state.clear()



@message_router.callback_query(ActionCallback.filter(F.command=="delete_user"))
async def callback_delete_user(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer("Enter the user ID you want to delete:")
    await state.set_state(UserFormState.delete)

@message_router.message(UserFormState.delete)
async def delete_user_by_id_message(message: types.Message, state: FSMContext):
    try:
        user_id = message.text
        result = await delete_user_by_id(user_id)
        if result:
            await message.answer(f"User with ID {user_id} deleted successfully.",  reply_markup=commands_keyboard)
        else:
            await message.answer(f"User with ID {user_id} not found.",  reply_markup=commands_keyboard)
    except ValueError:
        await message.answer("Invalid user ID. Please enter a valid numeric ID.",  reply_markup=commands_keyboard)
    except Exception as e:
        await message.answer(f"Error: {e}")
    finally:
        await state.clear()

@message_router.message()
async def update_user_data(message: types.Message, state: FSMContext):
    try:
        curr = await state.get_state()
        if curr == "waiting to update":
            user_id = (await state.get_data()).get("user_id")
            data = dict(item.split("=") for item in message.text.split(","))
            user = await update_user(user_id, **data)
            await message.answer(f"User updated:\n{user}",  reply_markup=commands_keyboard)
    except Exception as e:
        await message.answer(f"Error: {e}",  reply_markup=commands_keyboard)
    finally:
        await state.clear()

