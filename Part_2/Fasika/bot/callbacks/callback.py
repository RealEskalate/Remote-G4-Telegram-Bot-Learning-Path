from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, ForceReply
from aiogram import Router, types
from aiogram.fsm.context import FSMContext

from ..keyboards import keyboard

callback_router = Router()


@callback_router.callback_query(lambda c: c.data.startswith("action_1"))
async def process_callback_respond_to_action1(callback_query: types.CallbackQuery):
    await callback_query.message.answer(f"You've chosen {callback_query.data}! Great choice.")


@callback_router.callback_query(lambda c: c.data.startswith("action_2"))
async def process_callback_respond_to_action2(callback_query: types.CallbackQuery):
    await callback_query.message.answer(f"You've selected {callback_query.data}! That's awesome.")



@callback_router.callback_query(lambda c: c.data == "register_phone")
async def process_callback_register_phone(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer("📱 Please enter your phone number to register.", reply_markup=ForceReply())
    await state.set_state("waiting_for_phone")




@callback_router.callback_query(lambda c: c.data == "custom_action")
async def process_callback_custom_action(callback_query: types.CallbackQuery):
    await callback_query.message.answer("🚀 Performing a custom action.")