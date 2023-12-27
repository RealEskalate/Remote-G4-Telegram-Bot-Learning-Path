import asyncio
import logging
import sys 

from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage 
from bot.bot_instance import bot
from bot.handlers.message_handlers import message_router
from bot.handlers.registration_handlers import registration_router
from bot.callbacks.callback import callback_router


# def register_routers(dp: Dispatcher) -> None:
#     """Registers routers"""

#     dp.include_router(message_router)
#     dp.include_router(registration_router)

#     # callback routers
#     dp.include_router(callback_router)







storage = MemoryStorage()
async def main():

    dp = Dispatcher(storage=storage)
    dp.include_router(registration_router)
    dp.include_router(message_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())