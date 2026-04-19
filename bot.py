import asyncio
import logging
from aiogram import Bot, Dispatcher

from config import TOKEN
from handlers import start, create, help

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

start.register(dp)
create.register(dp)
help.register(dp)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
