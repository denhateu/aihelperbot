from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from dispatcher import dp
from task import Task


class Form(StatesGroup):
    delete_task_id = State()


@dp.message(Command("delete_task"))
async def delete_task_command_handler(message: Message, state: FSMContext) -> None:
    """
    This handler receives messages with `/delete_task` command
    """

    await state.clear()

    tasks = Task().get_all_tasks()

    result_string = ""
    for task in tasks:
        result_string += f"{task[0]}. {task[1]}\n"

    await message.answer(result_string)

    await message.answer("Выбери номер задачи")
    await state.set_state(Form.delete_task_id)


@dp.message(Form.delete_task_id)
async def delete_task_id_handler(message: Message, state: FSMContext) -> None:
    delete_task_id = message.text
    if delete_task_id:
        # Removing task from db
        Task().delete_task(delete_task_id)

        await message.answer("Задача удалена!")
        await state.clear()
