from os import getenv
from aiogram import Bot, types

# Use the commented code below if you store the token api in .env
from dotenv import load_dotenv

load_dotenv()

TOKEN_API = getenv("TOKEN_API")

# For hosting on pythonanywhere use the following commented code
# from aiogram.client.session.aiohttp import AiohttpSession

# bot = Bot(
#     token=TOKEN_API,
#     parse_mode="HTML",
#     session=AiohttpSession(proxy="http://proxy.server:3128"),
# )

# To run locally
bot = Bot(token=TOKEN_API, parse_mode="HTML")
