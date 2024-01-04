from aiogram.filters import Command
from aiogram import Router, types 
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext
from utils.state import Form

callback_router = Router()


@callback_router.callback_query(lambda c: c.data.startswith("name"))
async def process_name_change(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer("Enter new name:")
    await state.set_state(Form.update_name)
    

@callback_router.callback_query(lambda c: c.data == "age")
async def process_age_change(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer("Enter new age:")
    await state.set_state(Form.update_age)

@callback_router.callback_query(lambda c: c.data == "both")
async def process_age_change(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer("Enter new age:")
    await state.set_state(Form.update_both)
