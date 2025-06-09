from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from dispatcher import dp
from task import Task


class Form(StatesGroup):
    task_name = State()


@dp.message(Command("create_task"))
async def help_command_handler(message: Message, state: FSMContext) -> None:
    """
    This handler receives messages with `/create_task` command
    """

    await state.clear()

    await message.answer("Введи название задачи")
    await state.set_state(Form.task_name)

@dp.message(Form.task_name)
async def task_name_handler(message: Message, state: FSMContext) -> None:
    task_name = message.text

    # Adding task to db
    if task_name:
        task = Task()

        if task.task_name_exists(task_name) is False:
            task.create_task(task_name)

            await message.answer("Добавлено!")
            await state.clear()
        else:
            await message.answer("Такая задача уже есть")
    else:
        await message.answer("Не удалось добавить задачу")
