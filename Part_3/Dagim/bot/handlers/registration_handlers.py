import html
from aiogram.filters import Command
from aiogram import Router, types, F 
import aiogram.fsm.state
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    ContentType
)
from ..keyboards import keyboard
from utils.state import Form

registration_router = Router()

@registration_router.message(F.text.casefold() == "register")
async def start_handler(message: Message,state: FSMContext ):
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
    print(name) 
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
    await message.reply("all Done! You are now registered.", reply_markup=keyboard.show_profile_inline) 
        


@registration_router.message(Command('start'))
async def start_handler(message: types.Message):
    await message.answer("Hello Welcome to Telegram Bot Development Phase, Register and get our exculsive features :)", reply_markup=keyboard.register_reply_keyboard)
 
@registration_router.message(F.text == "Show-Profile")
async def start_handler(message: types.Message, state: FSMContext):
    curr_state = state.get_state()
    if curr_state is None:
        await message.answer("No User Found!", reply_markup=keyboard.register_reply_keyboard)
    else:
        data = await state.get_data()
        msg = str(f"First name: {data['first_name']}\nLast name: {data['last_name']},\nbio: {data['bio']}\nphone number: ||{data['phone_number']}||").replace("+", "\+")
        await  message.answer_photo(data["photo_id"],caption=msg, reply_markup=keyboard.logged_users_reply_keyboard, parse_mode="MarkdownV2" )



@registration_router.callback_query()
async def handle_inlines(call: types.CallbackQuery, state: FSMContext):
    curr_state = await state.get_state()
    print(curr_state)
    if curr_state is None:
        await call.message.answer("No User Found!", reply_markup=keyboard.register_reply_keyboard)
    if call.data == "handle_cancel":
        await state.clear()
        await   call.message.answer("Registeration has been canceled", reply_markup=keyboard.register_reply_keyboard)
    elif call.data == "handle_show_profile":
        
        data = await state.get_data()
        msg = str(f"First name: {data['first_name']}\nLast name: {data['last_name']},\nbio: {data['bio']}\nphone number: ||{data['phone_number']}||").replace("+", "\+")
        await  call.message.answer_photo(data["photo_id"],caption=msg, reply_markup=keyboard.logged_users_reply_keyboard, parse_mode="MarkdownV2" )
