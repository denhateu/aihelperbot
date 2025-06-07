from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from dispatcher import dp
from db import Database
from config_parser import config


class Form(StatesGroup):
    task_id = State()


async def show_tasks(message: Message):
    db = Database(config["database"]["name"])
    tasks = db.get_all_data("tasks")
    db.close()

    tasks_string = ""

    for task in tasks:
        tasks_string += f"{task[0]}. {task[1]}\n"

    await message.answer(tasks_string)


@dp.message(Command("edit_task"))
async def help_command_handler(message: Message, state: FSMContext) -> None:
    """
    This handler receives messages with `/edit_task` command
    """

    await state.clear()

    await show_tasks(message)

    await message.answer("Выбери номер задачи")
    await state.set_state(Form.task_id)


@dp.message(Form.task_id)
async def task_id_handler(message: Message, state: FSMContext) -> None:
    task_id = message.text

    if task_id != None:
        db = Database(config["database"]["name"])
        task_exists = db.check_if_data_exists("tasks", task_id)
        db.close()

        if task_exists:
            await message.answer("Изменено!")
            await state.clear()
        else:
            await message.answer("Такого номера задачи не существует!")
