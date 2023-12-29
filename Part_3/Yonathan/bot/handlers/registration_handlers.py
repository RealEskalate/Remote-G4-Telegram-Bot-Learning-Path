from aiogram.filters import Command
from aiogram import Router, types, F 
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ContentType
from aiogram.filters import Command

from ..keyboards import keyboard
from utils.state import Form

registration_router = Router()

@registration_router.message(Command('Register'))
async def start_handler(message: Message, state: FSMContext):
    try:
        await state.set_state(Form.country)
        await message.answer("Hello Welcome! What country are you from?")
    except:
        await message.answer("Something went wrong, don't worry it might be our fault.")

@registration_router.message(Form.country)
async def form_country(message: Message, state:FSMContext):
    try:
        await state.update_data(country=message.text)
        await state.set_state(Form.phone_number)
        await message.answer("May you give as your contact number!")
    except:
        await message.answer("Something went wrong, don't worry it might be our fault.")

@registration_router.message(Form.phone_number)
async def form_phone(message: Message, state:FSMContext):
    try:
        
        await state.update_data(phone_number = message.text)
        await state.set_state(Form.name)
        await message.answer("What's your name?")
    except:
        await message.answer("Something went wrong, don't worry it might be our fault.")

@registration_router.message(Form.name)
async def form_photo(message: Message, state:FSMContext):
    try:
        await state.update_data(name = message.text)
        await state.set_state(Form.bio)
        await message.answer("Tell as a little about your self. Will be recorded for you bio.")
    except:
        await message.answer("Something went wrong, don't worry it might be our fault.")

@registration_router.message(Form.bio)
async def form_photo(message: Message, state:FSMContext):
    try:
        await state.update_data(bio = message.text)
        await state.set_state(Form.photo)
        await message.answer("Care to share your photo. a happy one is perfered.")
    except:
        await message.answer("Something went wrong, don't worry it might be our fault.")

@registration_router.message(Form.photo, F.photo)
async def form_name(message: Message, state:FSMContext):
    try:
        photo_id = message.photo[-1].file_id
        data = await state.get_data()
        await state.clear()

        formatted_text = []
        [
            formatted_text.append(f"{key}: {value}")
            for key, value in data.items()
        ]

        await message.answer_photo(
            photo_id, "\n".join(formatted_text)
        )
    except:
        await message.answer("Something went wrong, don't worry it might be our fault.")