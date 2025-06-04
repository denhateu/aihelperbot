from aiogram.filters import CommandStart
from aiogram.types import Message

from dispatcher import dp
from texts import about_text


@dp.message(CommandStart())
async def start_command_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """

    await message.answer(f"Хай!\n{about_text}")
