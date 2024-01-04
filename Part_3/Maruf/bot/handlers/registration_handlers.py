from aiogram.filters import Command, CommandStart
from aiogram import Router, html, types, F 
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ContentType
from aiogram.filters import Command
from typing import Any, Dict
from ..keyboards import keyboard
from utils.state import Form

registration_router = Router()
    

@registration_router.message(Form.type_, F.casefold() == "pant")
async def process_pant(message: Message, state:FSMContext):
    try:
        await state.update_data(length=message.text)
        await state.set_state(Form.length)
        await message.answer("Your pant length: ")
    except:
        await message.answer("Some error occurred")

@registration_router.message(Form.type_, F.casefold() == "shirt")
async def process_shirt(message: Message, state:FSMContext):
    try:
        await state.update_data(lenght=message.text)
        await state.set_state(Form.sleeve_length)
        await message.answer("Your sleeve length: ")
    except:
        await message.answer("Some error occurred")


@registration_router.message(Form.phone_number)
async def process_phone(message: Message, state:FSMContext):
    try:
        
        await state.update_data(phone_number = message.text)
        await state.set_state(Form.type_)
        await message.answer("What do you want", reply_markup=keyboard.type_request_keyboard)
    except:
        await message.answer("Some error occurred")

@registration_router.message(Form.length)
async def process_length(message: Message, state:FSMContext):
    try:
        
        await state.update_data(length = message.text)
        await state.set_state(Form.hip)
        await message.answer("your hip size:")
    except:
        await message.answer("Some error occurred")

@registration_router.message(Form.hip)
async def process_hip(message: Message, state:FSMContext):
    try:
        
        await state.update_data(hip = message.text)
        await state.set_state(Form.waist)
        await message.answer("your waist size:")
    except:
        await message.answer("Some error occurred")

@registration_router.message(Form.waist)
async def process_waist(message: Message, state:FSMContext):

    print("b4 update")
    data = await state.update_data(waist = message.text)
    print("after update")
    await show_summary(message=message, data=data)
    await state.clear()


@registration_router.message(Form.name)
async def process_name(message: Message, state: FSMContext) -> None:
    try:
        await state.update_data(name=message.text)
        await state.set_state(Form.phone_number)
        await message.answer(text=f"Nice to meet you {message.text},\nGive us your phone number."
        )
    except:
        await message.answer("Some error occurred")



@registration_router.message(Form.sleeve_length)
async def process_sleeve_length(message: Message, state:FSMContext):
    try:
        await state.update_data(sleeve_length = message.text)
        await state.set_state(Form.body_length)
        await message.answer("your body length:")
    except:
        await message.answer("Some error occurred")


@registration_router.message(Form.body_length)
async def process_body_length(message: Message, state:FSMContext):
    try:
        await state.update_data(body_length = message.text)
        await state.set_state(Form.chest_width)
        await message.answer("your chest width:")
    except:
        await message.answer("Some error occurred")

@registration_router.message(Form.chest_width)
async def process_chest_width(message: Message, state:FSMContext):
    try:
        data = await state.update_data(chest_width = message.text)
        await show_summary(message=message, data=data)
        await state.clear()
    except:
        await message.answer("Some error occurred")

async def show_summary(message: Message, data: Dict[str, Any]) -> None:
    name = data["name"]
    p_number = data["phone_number"]
    preference = data["type_"]
    summary_text = f"Name: {name}\nPhone: {p_number}\nPreference: {preference}"
    if preference == "shirt":
        sl = data["sleeve_length"]
        cw = data["chest_width"]
        bl = data["body_length"]
        summary_text += f"\nSleeve Length: {sl}"
        summary_text += f"\nChest Width: {cw}"
        summary_text += f"\nBody Length: {bl}"
    if preference == "pant":
        l = data["length"]
        w = data["waist"]
        h = data["hip"]
        summary_text += f"\nLength: {l}"
        summary_text += f"\nWaist: {w}"
        summary_text += f"\nHip: {h}"
    await message.answer(text=summary_text)