from aiogram.filters import CommandStart
from aiogram.types import Message

from dispatcher import dp
from texts import about_text
from db import Database
from config_parser import config


@dp.message(CommandStart())
async def start_command_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """

    # Initialize database connection
    db = Database(config["database"]["name"])

    # Creates tables if not exists
    db.execute_query(f"""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")

    db.close()

    await message.answer(f"Хай!\n{about_text}")
