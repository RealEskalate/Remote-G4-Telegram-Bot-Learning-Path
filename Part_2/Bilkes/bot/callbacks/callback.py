from aiogram.filters import Command
from aiogram import Router, types 
from aiogram.utils.keyboard import InlineKeyboardBuilder

from aiogram.types import ReplyKeyboardRemove
callback_router = Router()




@callback_router.callback_query(lambda c: c.data=="register_phone")
async def process_callback_respond_to_phone(callback_query: types.CallbackQuery):
    await callback_query.message.answer(f"Please enter your Phone Number",)


@callback_router.callback_query(lambda c: c.data=="register_location")
async def process_callback_respond_to_location(callback_query: types.CallbackQuery):
    await callback_query.message.answer(f"Please enter your location",)
