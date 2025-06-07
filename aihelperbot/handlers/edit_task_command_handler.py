from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from dispatcher import dp
from task import Task


class Form(StatesGroup):
    task_id = State()
    new_task_name = State()


@dp.message(Command("edit_task"))
async def help_command_handler(message: Message, state: FSMContext) -> None:
    """
    This handler receives messages with `/edit_task` command
    """

    await state.clear()

    tasks = Task().get_all_tasks()

    result_string = ""
    for task in tasks:
        result_string += f"{task[0]}. {task[1]}\n"

    await message.answer(result_string)

    await message.answer("Выбери номер задачи")
    await state.set_state(Form.task_id)


@dp.message(Form.task_id)
async def task_id_handler(message: Message, state: FSMContext) -> None:
    task_id = message.text
    if task_id:
        # Saves task id in FSM memory
        await state.update_data(id=task_id)

        await message.answer("Введи новое название задачи")

        await state.set_state(Form.new_task_name)


@dp.message(Form.new_task_name)
async def new_task_name_handler(message: Message, state: FSMContext) -> None:
    new_task_name = message.text
    if new_task_name:
        # Gets data from FSM memory
        data = await state.get_data()
        task_id = data.get("id")

        Task().edit_task(str(task_id), new_task_name)

        await message.answer("Изменено!")
        await state.clear()
