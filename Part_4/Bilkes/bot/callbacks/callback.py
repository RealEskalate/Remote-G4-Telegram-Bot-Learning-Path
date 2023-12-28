from aiogram.filters import Command
from aiogram import Router, types 
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ContentType


from utils.state import Form

callback_router = Router()




@callback_router.callback_query(lambda c: c.data=="register")
async def process_callback_respond_to_register(callback_query: types.CallbackQuery,message: Message, state: FSMContext):
    await callback_query.message.answer(f"Let's Start registration",)

# async def name_form(message: Message, state: FSMContext):
    try:
        await message.answer("Here you be providing your required information in order to be registered 🙂")
        await state.set_state(Form.name)
        await message.answer("Enter Your Name : ")
    except:
        await message.answer("Some error occurred")
