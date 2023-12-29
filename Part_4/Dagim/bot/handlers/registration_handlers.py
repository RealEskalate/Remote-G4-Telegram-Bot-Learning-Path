import html
from aiogram.filters import Command
from aiogram import Dispatcher, Router, types, F 
import aiogram.fsm.state
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    ContentType,
    user,
)

from bot import bot_instance
from  ..init_sqlite import * 
from ..keyboards import keyboard
from utils.state import Form

registration_router = Router()




@registration_router.message(F.text == 'Refresh')
async def handle_refresh(message: types.Message, state: FSMContext):
    await state.clear()
    await state.update_data(user_id=message.from_user.id)
    await message.delete()
    
    data = await state.get_data()
    userID = data["user_id"]
    # print("from refresh", data, userID)
    # 2103092364
    # 2103092364
    status = await get_profile(str(userID))
    # print("->>>>",status)
    if not status:
        await message.answer("User not found, Please Register", reply_markup=keyboard.register_reply_keyboard)
    else:
        # print( status)
        await state.update_data(user_id=status[1])
        await message.answer("Welcome Back, " + status[2], reply_markup=keyboard.logged_users_reply_keyboard)





@registration_router.message(F.text.casefold() == "register")
async def start_handler(message: Message,state: FSMContext ):
    
    # print(message.from_user.id)
    await state.update_data(user_id=message.from_user.id)
    await state.set_state(Form.first_name)
    await message.answer("Hello Welcome, let's give you some account \n if you don't wish to continue, you can send /cancel at anytime.")
    await message.answer("Please enter your first name", reply_markup=keyboard.cancel_inline_keyboard)


@registration_router.message(Form.first_name)
async def form_handle_first_name(message: Message, state: FSMContext):
    
    await state.update_data(first_name=message.text)
    await state.set_state(Form.last_name)
    await message.answer("Last Name please: ", reply_markup=keyboard.cancel_inline_keyboard)




@registration_router.message(Form.last_name)
async def form_handle_last_name(message: Message, state: FSMContext):
    
    await state.update_data(last_name=message.text)
    await state.set_state(Form.phone_number)
    await message.answer("register your phone,", reply_markup=keyboard.register_phone_keyboard)


# handle cancel or any other action for last_name 


@registration_router.message(F.content_type.in_({'contact', 'CONTACT'}), Form.phone_number,)
async def form_phone(message: Message, state: FSMContext):
   
    await state.update_data(phone_number=message.contact.phone_number)
    await state.set_state(Form.bio)
    name = await state.get_data()
    # print(name) 
    await message.answer(f"alright {name['first_name']}, Give me some description about you, please", reply_markup=keyboard.cancel_inline_keyboard)


@registration_router.message(Form.bio)
async def form_handle_bio(message: Message, state: FSMContext):
    
    await state.update_data(bio = message.text)
    await state.set_state(Form.photo)
    await message.answer("Let's set your profile picture, send me a picture", reply_markup=keyboard.cancel_inline_keyboard)


@registration_router.message(Form.photo, F.photo)
async def form_name(message: Message, state :FSMContext):
    

    photo_id = message.photo[-1].file_id
    await state.update_data(photo_id=photo_id)
    data = await state.get_data()
    # print("saving userid: ", data['user_id'], " =>", message.from_user.id )
    
    status = await create_profile(str(data['user_id']),data['first_name'],data['last_name'], data['bio'] ,data['phone_number'], data['photo_id'] )
    
    if status:
        await message.answer("✅Account Created",reply_markup=keyboard.show_profile_inline)
        # await state.clear()
        # s = await state.get_state()?
    else:
        
        await message.answer("⚠️Something Went Wrong",reply_markup=keyboard.register_reply_keyboard)


    # print("user data: ", data)

        


@registration_router.message(Command('start'))
async def start_handler(message: types.Message, state: FSMContext):
    curr_state = await state.get_state()
    if curr_state:
        data = curr_state.get_data()
        # print("Start" , data)
        if data:
            user =await get_profile(data["user_id"])
            if user: 
                await message.answer("👋Welcome back," + user[2], reply_markup=keyboard.logged_users_reply_keyboard)
        else:
            await message.answer("Register here please, ", reply_markup=keyboard.register_reply_keyboard)
    else:
        await message.answer("Hello Welcome to Telegram Bot Development Phase, Register and get our exculsive features :) \n Hit Refresh to Login with one click", reply_markup=keyboard.register_and_refresh_reply_keyboard)
 
@registration_router.message(F.text == "Show-Profile")
async def start_handler(message: types.Message, state: FSMContext):
    
    await state.update_data(user_id=message.from_user.id)
    await message.delete()

    #handle if there is state or not 
    curr_state = await state.get_state()
    if curr_state: 
        state_data = await state.get_data()
        # print(not state_data, "on show-profile")
        if not state_data :
            # print("inside")
            await message.answer("You are not logged in. Please try to login or register again.", reply_markup=keyboard.register_and_refresh_reply_keyboard)
        else:     


            data = await get_profile(state_data['user_id'])
           
            msg = str(f"First name: {data[2]}\nLast name: {data[3]},\nbio: {data[4]}\nphone number: ||{data[5]}||").replace("+", "\+")
            await  message.answer_photo(data[6],caption=msg, reply_markup=keyboard.logged_users_reply_keyboard, parse_mode="MarkdownV2" )
    else:
        msg = "✋You are not logged in. Please `Refresh`  to login with one click or register.".replace(".", "\.")
        await message.answer(msg, parse_mode="MarkdownV2", reply_markup=keyboard.register_and_refresh_reply_keyboard)

@registration_router.message(F.text == "Delete Profile")
async def start_handler(message: types.Message, state: FSMContext):
    await message.delete()
    # print("on delete profile")
    #handle if there is state or not 
    
    curr_state = await state.get_state()
    # print(curr_state)
    if curr_state: 
        # print("got state")
        state_data = await state.get_data()
        # print(not state_data, "on show-profile")
        if not state_data :
            # print("inside")
            await message.answer("You are not logged in. Please try to login or register again.", reply_markup=keyboard.register_and_refresh_reply_keyboard)
        else:     


            data = await get_profile(state_data['user_id'])
            if data: 
                # if the user exist, then delete 
                delete = await delete_profile(state_data['user_id'])
                if delete:
                    await state.clear()
                    await message.answer("Profile deleted successfully🗑", reply_markup=keyboard.register_and_refresh_reply_keyboard )
            else:
                await message.answer("⚠️Something Went Wrong, Try again",reply_markup=keyboard.logged_users_reply_keyboard)
                # print("No data found")

    else:
        msg = "✋You are not logged in. Please `Refresh`  to login with one click or register.".replace(".", "\.")
        await message.answer(msg, parse_mode="MarkdownV2", reply_markup=keyboard.register_and_refresh_reply_keyboard)


@registration_router.callback_query()
async def handle_inlines(call: types.CallbackQuery, state: FSMContext,) -> None:
    if call.data == "handle_cancel":
        await state.clear()
        await   call.message.answer("Registeration has been canceled", reply_markup=keyboard.register_reply_keyboard)
    
    curr_state = await state.get_state()
    # print(curr_state)
    if curr_state is None:
        await call.message.answer("You are not logged in. Please try to login or register again.", reply_markup=keyboard.register_and_refresh_reply_keyboard)
    # elif call.data == "handle_show_profile":
        
        # data = await state.get_data()
    if call.data == "handle_show_profile":
        # print("=> " ,dir(call.messsage ))
        
        state_data = await state.get_data()
        # print(not state_data, "on show-profile")
        if not state_data :
            # print("inside")
            await call.message.reply("You are not logged in. Please try to login or register again.", reply_markup=keyboard.register_and_refresh_reply_keyboard)
        else:     


            data = await get_profile(state_data['user_id'])
            
            msg = str(f"First name: {data[2]}\nLast name: {data[3]},\nbio: {data[4]}\nphone number: ||{data[5]}||").replace("+", "\+")
            await  call.message.answer_photo(data[6],caption=msg, reply_markup=keyboard.logged_users_reply_keyboard, parse_mode="MarkdownV2" )


async def handle_state():
    state = FSMContext
    message = types.Message
    curr = await state.get_state(state)
    if not curr: 
        await state.clear()
        message.answer("You are not logged in. Please try to login or register again.", reply_markup=keyboard.register_and_refresh_keyboard)
    else:
        data = await state.get_data()
        if not data:
            message.answer("You are not logged in. Please try to login or register again.", reply_markup=keyboard.register_and_refresh_keyboard)
        


