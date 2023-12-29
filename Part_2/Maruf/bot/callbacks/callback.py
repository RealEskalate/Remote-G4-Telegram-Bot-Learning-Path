from aiogram.filters import Command
from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder


callback_router = Router()

@callback_router.callback_query(lambda c: c.data == "phone")
async def register_phone_handler(
    callback_query: types.CallbackQuery, state: FSMContext
):
    await callback_query.message.answer("Please share your phone number.")
    await state.set_state("phone")


@callback_router.callback_query(lambda c: c.data == "name")
async def custom_action_handler(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer("Please share your name.")
    await state.set_state("name")
