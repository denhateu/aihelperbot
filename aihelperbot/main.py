import sys
import logging
from os import getenv
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message


# Gets token from environment
TOKEN = getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()


about_text = """
Мой AI-помощник - это телеграм-бот, который поможет тебе в планировании задач и т.д. Бот поддерживает управление как текстом так и ГОЛОСОМ!"""


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """

    await message.answer(f"Хай!\n{about_text}")


@dp.message(Command("help"))
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/help` command
    """

    await message.answer(f"""{about_text}

Доступные команды:
/start - выводит приветствие и описание бота
/help - описание бота и список доступных команд
/create_task - создает новую задачу
/edit_task - изменяет существующую задачу
/delete_task - удаляет задачу
/tasks - показывает все задачи
""")


async def main() -> None:
    # Run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
