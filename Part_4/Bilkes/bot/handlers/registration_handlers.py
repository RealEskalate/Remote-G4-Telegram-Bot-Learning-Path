from aiogram.filters import Command
from aiogram import Router, types, F 
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ContentType
from aiogram.filters import Command
from datetime import datetime
from ..keyboards import keyboard
from utils.state import Form
from database.services.user_services import  create_user

registration_router = Router()


@registration_router.message(Command('Register'))
async def name_form(message: Message, state: FSMContext):
    print(message.text)
    
    try:
        await message.answer("Here you will be providing your required information in order to be registered 🙂")
        await state.set_state(Form.name)
        await message.answer("Enter Your Name : ")
    except:
        await message.answer("Some error occurred")


@registration_router.message(Form.name)
async def phone_form(message: Message, state:FSMContext):
    try:
        await state.update_data(name=message.text)
        await state.set_state(Form.photo_id)
        await message.answer("Let's Continue with your profile pic")
    except:
        await message.answer("Some error occurred")

@registration_router.message(Form.photo_id)
async def age_form(message: Message, state:FSMContext):
    try:
        
        await state.update_data(photo_id = message.photo[-1].file_id)
        await state.set_state(Form.age)
        await message.answer("Now enter your age")
    except:
        await message.answer("Some error occurred")
@registration_router.message(Form.age)
async def phone_form(message: Message, state:FSMContext):
    try:
        
        await state.update_data(age = message.text)
        await state.set_state(Form.phone_number)
        await message.answer("Enter your phone number")
    except:
        await message.answer("Some error occurred")

@registration_router.message(Form.phone_number)
async def form_photo(message: Message, state:FSMContext):
    try:
        await state.update_data(phone_number = message.text)
        

        data=await state.get_data()


        print("Adding user...")
        users = await create_user(int(message.chat.id), name=data['name'],phone_number=data['phone_number'],photo_id=data['photo_id'],age=data['age'] ,date=datetime.now())
        print("done")
        await message.answer("You have been successfully register👏")
        await message.answer("Now you are allowed to check the following services")
        await message.answer("/get_all_users   -> View the list of Registered User")


    except Exception as e:

        await message.answer(f"Some error occurred {e}")

