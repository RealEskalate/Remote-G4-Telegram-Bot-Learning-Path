import motor.motor_asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from os import getenv

from dotenv import load_dotenv

load_dotenv()

MONGO_URL = getenv("MONGO_URL")


cluster = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
collection = cluster.Cluster0
