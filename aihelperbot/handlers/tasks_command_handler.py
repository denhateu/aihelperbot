from aiogram.filters import Command
from aiogram.types import Message

from dispatcher import dp
from task import Task


@dp.message(Command("tasks"))
async def tasks_command_handler(message: Message) -> None:
    """
    This handler receives messages with `/tasks` command
    """

    await Task().show_tasks(message)
