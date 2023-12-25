import os
from aiogram import Bot, types
from dotenv import load_dotenv
load_dotenv()


# For hosting on pythonanywhere use the following commented code
from aiogram.client.session.aiohttp import AiohttpSession
bot = Bot(
    token=os.environ.get("TOKEN"),
    parse_mode='HTML',
    session=AiohttpSession(proxy='http://proxy.server:3128')
)

# bot = Bot(
#     token=os.environ.get("TOKEN"),
#     parse_mode='HTML'
# )