import asyncio
from aiogram import Dispatcher
from bot_instance import bot
from handlers.user_handlers import user_router

def register_routers(dp:Dispatcher) -> None:
  """Registers router"""
  dp.include_routers(user_router)

async def main() -> None:
  dp = Dispatcher()
  register_routers(dp)
  await dp.start_polling(bot)

if __name__ == "__main__":
  asyncio.run(main())