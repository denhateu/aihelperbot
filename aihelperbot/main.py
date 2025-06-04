import sys
import logging
from dotenv import load_dotenv
import os
import asyncio
from aiogram import Bot

from dispatcher import dp
import handlers


# Gets token from environment
load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)


async def main() -> None:
    # Run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
