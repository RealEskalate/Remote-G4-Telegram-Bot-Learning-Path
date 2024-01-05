from aiogram.filters import Command
from aiogram import Router, types 
from aiogram.utils.keyboard import InlineKeyboardBuilder


callback_router = Router()


callback_router.callback_query(lambda c: c.data=="register")
async def register_callback(callback_query: types.CallbackQuery,message: Message, state: FSMContext):
    await callback_query.message.answer(f"Let's Start registration",)
    try:
        await message.answer("Enter info for registration")
        await state.set_state(Form.name)
        await message.answer("Name : ")
    except:
        await message.answer("Some error occurred")