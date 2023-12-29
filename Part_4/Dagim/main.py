import asyncio
import logging
import sys
from bot.init_sqlite import start_db 
from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from bot.bot_instance import bot
from bot.handlers.message_handlers import message_router
from bot.handlers.registration_handlers import registration_router
from bot.callbacks.callback import callback_router

async def on_startup(_):
    print("Starting")
    await start_db()


async def main():
    storage = MemoryStorage()
    # bot.session.middleware(CustomMiddleware())

    dp = Dispatcher(storage=storage)
    
    dp.include_router(registration_router)
    dp.include_router(message_router)
    await start_db()
    
    # dp.update.middleware.register(CustomMiddleware(dp))
    # print(dir(dp.update.middleware))
    # Add on_startup to run functions at the start of the bot
    await dp.start_polling(bot, )

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
