from aiogram.filters import Command
from aiogram.types import Message

from dispatcher import dp
from texts import about_text


@dp.message(Command("help"))
async def help_command_handler(message: Message) -> None:
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
