from aiogram.filters import Command
from aiogram import Router, types
from aiogram.fsm.context import FSMContext 
from aiogram.utils.keyboard import InlineKeyboardBuilder

from ..keyboards import keyboard


callback_router = Router()


@callback_router.callback_query(lambda c: c.data.startswith("action_1"))
async def process_callback_respond_to_action1(callback_query: types.CallbackQuery):
    await callback_query.message.answer(f"you picked {callback_query.data}")

@callback_router.callback_query(lambda c: c.data.startswith("action_2"))
async def process_callback_respond_to_action1(callback_query: types.CallbackQuery):
    await callback_query.message.answer(f"you picked {callback_query.data}")

# Add a cancel registration command handler
@callback_router.callback_query(lambda c: c.data.startswith("cancel regestration"))
async def cancel_registration_handler(callback_query: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await callback_query.message.answer("Registration canceled. Type /start to start again.", reply_markup=keyboard.reply_keyboard)
