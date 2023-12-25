from aiogram.filters import Command
from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder


callback_router = Router()


@callback_router.callback_query(lambda c: c.data.startswith("action_1"))
async def process_callback_respond_to_action1(callback_query: types.CallbackQuery):
    await callback_query.message.answer(f"you picked {callback_query.data}")


@callback_router.callback_query(lambda c: c.data.startswith("action_2"))
async def process_callback_respond_to_action1(callback_query: types.CallbackQuery):
    await callback_query.message.answer(f"you picked {callback_query.data}")


@callback_router.callback_query(lambda c: c.data == "register_phone")
async def register_phone_handler(
    callback_query: types.CallbackQuery, state: FSMContext
):
    await callback_query.message.answer("Please share your phone number.")
    await state.set_state("waiting_for_phone")


@callback_router.callback_query(lambda c: c.data == "custom_button")
async def custom_action_handler(callback_query: types.CallbackQuery):
    await callback_query.message.answer("You clicked the custom button.")
