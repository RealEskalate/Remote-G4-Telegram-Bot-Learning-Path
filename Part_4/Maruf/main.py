import asyncio 

from aiogram import Dispatcher
from bot.bot_instance import bot
from pymongo.mongo_client import MongoClient
import certifi
from bot.handlers.message_handlers import message_router
from bot.callbacks.callback import callback_router
from database.loader import collection

def register_routers(dp: Dispatcher) -> None:
    """Registers routers"""

    dp.include_router(message_router)
    
    # callback routers
    dp.include_router(callback_router)





async def main() -> None:
    """The main function which will execute our event loop and start polling."""

    try:
        dp = Dispatcher()

        print('Bot Starting....')
        register_routers(dp)
        print("Polling ....")
        await dp.start_polling(bot)
        
    except Exception as e:
        print(f"Some error occurred\n{e}")
    

if __name__ == "__main__":
    asyncio.run(main())
