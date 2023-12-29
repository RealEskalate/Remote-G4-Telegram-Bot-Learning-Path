from aiogram.filters import Command
from aiogram import Router, types, F 
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext

from bot.gen_meme import Genmeme

from ..keyboards import keyboard

message_router = Router()

@message_router.message(F.USER)
async def message_route(message: types.Message, state: FSMContext):
    print()
    await message.answer("user id is ")
# @message_router.callback_query()
# async def handle_inlines(call: types.CallbackQuery):
    
#     if call.data == "memes_handler":
#         image_url = memegenerate()  
#         await call.message.answer_photo(image_url, reply_to_message_id=call.message.message_id)


#     else:
        
#         await call.message.answer("Not working")

@message_router.message(F.text=='Chat')
async def get_image(message: types.Message):
    try:
        image_url = memegenerate()  
        await message.answer("⚠️ Feature under construction!", reply_to_message_id=message.message_id)
    except:
        await message.answer("Network error! Try again")



@message_router.message(F.text=='Get-Memes')
async def get_image(message: types.Message):
    await message.delete()
    image_url = memegenerate()  
    await message.answer_photo( image_url, )


def memegenerate():
    g = Genmeme().generate()
    return g