import io
from aiogram.filters import Command
from aiogram import Router, types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import KeyboardButton, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup
from bot.gen_meme import Genmeme
import aiohttp
from bot.bot_instance import bot as b_bot


message_router = Router()

btn1 = KeyboardButton(text="Phone Number", request_contact=True)
btn2 = KeyboardButton(text="Location", request_location=True)
btn3 = KeyboardButton(text="Get memes")
btn4 = KeyboardButton(text="Inline Buttons")

keyboard_reply = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, keyboard=[[btn1], [btn2], [btn3], [btn4]])

@message_router.message(Command('start'))
async def start_handler(message: types.Message):
    
    await message.answer("Hello Welcome, Quick Start, Choose:", reply_markup=keyboard_reply)
    await message.delete()

@message_router.message(Command('help'))
async def help_handler(message: types.Message):
    await message.reply("Hello, This is a Help command\n type /start - to get started\n /chat - to start chatting")

@message_router.message(Command('chat'))
async def chat_handler(message: types.Message):
    await message.reply("Currently am not working, I will be implemented soon :) ")

@message_router.message(F.content_type.in_({'contact', 'CONTACT'}))
async def handle_contact_reply_btns(message: types.Message):
    phone_number = message.contact.phone_number
    await message.answer(f"Thanks, you are now registered\nYour phone number is: {phone_number}")
    await message.answer("Hello Welcome, Quick Start, Choose:", reply_markup=keyboard_reply)
    

@message_router.message(F.location | F.LOCATION)
async def handle_location_reply_btns(message: types.Message):
    await message.answer("Thanks for sharing your location")

@message_router.message(F.text == "Inline Buttons")
async def pop_inline_btns(message: types.Message):
    await message.delete()
    await message.answer("Hello Welcome, Quick Start, Choose:", reply_markup=inline_keyboard)



@message_router.message(F.text == "Get memes")
async def send_memes(message: types.Message):
   image_url = memegenerate() 
   await message.answer_photo(image_url, reply_to_message_id=message.message_id) 


# INLINE BUTTONS
btn_inline_phone = InlineKeyboardButton(text="Phone Number", callback_data="phone_number_handler", request_contact=True)
btn_inline_loc = InlineKeyboardButton(text="Location", callback_data="location_handler")
btn_inline_memes = InlineKeyboardButton(text="Get memes", callback_data="memes_handler")

inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[[btn_inline_phone], [btn_inline_loc], [btn_inline_memes]], resize_keyboard=True, one_time_keyboard=True)

@message_router.message(Command('inline'))
async def inline_handler(message: types.Message):
    await message.reply("Hello Welcome, Quick Start Register with: ", reply_markup=inline_keyboard)

@message_router.callback_query()
async def handle_inlines(call: types.CallbackQuery):
    if call.data == "phone_number_handler":
        await call.message.answer("Please share your phone number by tapping the button below:", reply_markup=ReplyKeyboardMarkup(
            keyboard=[[btn1]],
            resize_keyboard=True,
            one_time_keyboard=True,
        ))
    elif call.data == "location_handler":
       await call.message.answer("Please share your Location by tapping the button below:", reply_markup=ReplyKeyboardMarkup(
            keyboard=[[btn2]],
            resize_keyboard=True,
            one_time_keyboard=True,
        ))
    elif call.data == "memes_handler":
        image_url = memegenerate()  # Replace with the actual URL of the image
        await call.message.answer_photo(image_url, reply_to_message_id=call.message.message_id)


    else:
        
        await call.message.answer("Not working")

@message_router.message(Command('jo-memes'))
async def get_image(message: types.Message):
    image_url = memegenerate()  # Replace with the actual URL of the image
    await message.answer_photo( image_url, reply_to_message_id=message.message_id)


def memegenerate():
    g = Genmeme().generate()
    return g