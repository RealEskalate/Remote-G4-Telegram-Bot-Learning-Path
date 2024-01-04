from aiogram import Bot, Dispatcher
import certifi
from pymongo.mongo_client import MongoClient

from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
import os
load_dotenv()
MONGO_URL = os.environ.get("MONGO_URL")


cluster = MongoClient(MONGO_URL, tlsCAFile=certifi.where())
db = cluster["user_db"]
collection = db["user_info"]
