from aiogram.filters import Command
from aiogram import Router, types 
import urllib
from aiogram.methods.send_photo import SendPhoto
from utils.state import Form
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ContentType
from bot.bot_instance import bot
callback_router = Router()
@callback_router.callback_query(lambda c: c.data.startswith("register"))
async def process_registration(callback_query: types.CallbackQuery, state: FSMContext):
    try:
        await state.set_state(Form.name)
        await callback_query.message.answer("Hello Welcome to  our tailor shop, Tell us your name: ")
    except:
        await callback_query.answer("Some error occurred")


@callback_router.callback_query(lambda c: c.data.startswith("pant"))
async def process_pant(callback_query: types.CallbackQuery, state: FSMContext):
    try:
        await state.update_data(type_="pant")
        await state.set_state(Form.length)
        await callback_query.message.answer("your pant length: ")
    except:
        await callback_query.answer("Some error occurred")

@callback_router.callback_query(lambda c: c.data.startswith("shirt"))
async def process_shirt(callback_query: types.CallbackQuery, state: FSMContext):
    try:
        await state.update_data(type_="shirt")
        await state.set_state(Form.sleeve_length)
        await callback_query.message.answer("your shirt sleeve length: ")
    except:
        await callback_query.answer("Some error occurred")



@callback_router.callback_query(lambda c: c.data.startswith("explore"))
async def handle_explore(callback_query: types.CallbackQuery):
    async def send_photo_grid(chat_id, photo_urls):
        media_group = []
        for url in photo_urls:
            await bot(SendPhoto(chat_id=chat_id, photo=url))
            
    
    async def explore_photos_callback(callback_query: types.CallbackQuery):
        await callback_query.answer()  # Acknowledge (if needed)
        user_id = callback_query.from_user.id
        
        photo_urls = [
            "https://i.ibb.co/QKmPXh3/emmanuel-boldo-u3-Cm8y-J0-Hj-E-unsplash.jpg",
            "https://i.ibb.co/xhKXKpW/andrea-natali-jd-Ttkmr1axk-unsplash.jpg",
            "https://i.ibb.co/RyBdPZY/maude-frederique-lavoie-EDSTj4k-CUcw-unsplash.jpg",
            "https://i.ibb.co/524W9fr/clem-onojeghuo-kg3-N8vqv-Md8-unsplash.jpg",
            "https://i.ibb.co/RHFd00T/nimble-made-7-RIMS-NMsbc-unsplash.jpg",
            "https://i.ibb.co/ZmDJSjp/nimble-made-BKYe-LLB1-Ox-I-unsplash.jpg",
            "https://i.ibb.co/qRCtTxm/nimble-made-Jf7-Jq-Vazm-4-unsplash.jpg",
        ]
        
        await send_photo_grid(user_id, photo_urls)

    await explore_photos_callback(callback_query)