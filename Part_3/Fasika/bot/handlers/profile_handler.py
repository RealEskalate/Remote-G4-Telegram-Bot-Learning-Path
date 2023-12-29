from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from ..keyboards.profile import profile_markup

async def show_profile_handler(message: Message, state: FSMContext):
    try:
        data = await state.get_data()
        if not data:
            await message.answer("You haven't registered yet. Type /start to start.")
            return

        photo_id = data.get("photo_id")
        formatted_text = [f"{key}: {value}" for key, value in data.items() if key != "photo_id"]

        if photo_id:
            await message.answer_photo(photo_id, "\n".join(formatted_text), reply_markup=profile_markup)
        else:
            await message.answer("\n".join(formatted_text), reply_markup=profile_markup)
    except Exception as e:
        await message.answer(f"An error occurred: {e}")
