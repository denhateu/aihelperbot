from aiogram.filters import Command
from aiogram.types import Message

from dispatcher import dp
from task import Task


@dp.message(Command("tasks"))
async def tasks_command_handler(message: Message) -> None:
    """
    This handler receives messages with `/tasks` command
    """

    tasks = Task().get_all_tasks()

    result_string = "Список задач:\n"
    for task in tasks:
        result_string += f"{task[0]}. {task[1]}\n"

    await message.answer(result_string)
