import os
from aiogram import Bot, Dispatcher
import motor.motor_asyncio
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
load_dotenv()

# from config import MONGO_URL

MONGO_URL=os.getenv('MONGO_URL')

cluster = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
collection = cluster.Test.newCollection
