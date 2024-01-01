import os
from aiogram import Bot, types

from config import TOKEN_API


bot = Bot(
    token=TOKEN_API,
    parse_mode='HTML'
)