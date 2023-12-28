from aiogram import Router, types


callback_router = Router()


@callback_router.callback_query(lambda c: c.data == "register_phone")
async def process_custom_inline_button_1(callback_query: types.CallbackQuery):
    await callback_query.answer("You clicked on Custom register phone button")
    await callback_query.message.answer(f"you picked {callback_query.data}")


@callback_router.callback_query(lambda c: c.data == "share_location")
async def process_custom_inline_button_2(callback_query: types.CallbackQuery):
    await callback_query.answer("You clicked on register location button")
