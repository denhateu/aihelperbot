from aiogram.types import Message

from db import Database
from config_parser import config


class Task:
    """
    This is class for manage tasks, including create, read,
    edit, delete and etc
    """

    def __init__(self) -> None:
        """
        When class initializing, then create tasks table if this table
        not exists in database
        """

        # Initialize database connection
        db = Database(config["database"]["name"])

        # Creates tasks table if not exists
        db.execute_query(f"""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")

        db.close()

    def task_id_exists(self, task_id: str) -> bool:
        """
        Checks if task ID is exists in database

        Args:
            task_id:
                Task identificator, this is number from 1 to ...

        Returns:
            True - if task ID exists in database
            False - if task ID not exists in database
        """

        # Initialize database connection
        db = Database(config["database"]["name"])
        task = db.fetch_one(f"SELECT * FROM tasks WHERE id = ?", (task_id,))
        db.close()

        if task == None:
            return False
        else:
            return True

    def task_name_exists(self, task_name: str) -> bool:
        """
        Checks if task name is exists in database

        Args:
            task_name:
                This is any string

        Returns:
            True - if task name exists in database
            False - if task name not exists in database
        """

        # Initialize database connection
        db = Database(config["database"]["name"])
        task = db.fetch_one(f"SELECT * FROM tasks WHERE name = ?", (task_name,))
        db.close()

        if task == None:
            return False
        else:
            return True

    def create_task(self, task_name: str) -> None:
        """
        Adds a new task to the table

        Args:
            task_name:
                Any string
        """

        # Initialize database connection
        db = Database(config["database"]["name"])

        db.execute_query(f"""
INSERT INTO tasks (name)
VALUES (?)
""", (task_name,))

        db.close()

    def edit_task(self, task_id: str, task_name: str) -> None:
        """
        Changes task name from old name to new name in table using task ID

        Args:
            task_id:
                Task identificator, this is number from 1 to ...
            task_name:
                Any string
        """

        # Initialize database connection
        db = Database(config["database"]["name"])

        db.execute_query(f"""
UPDATE tasks
SET name = ?
WHERE id = ?
""", (task_name, task_id))

        db.close()

    def delete_task(self, task_id: str) -> None:
        """
        Removes task from table using task ID

        Args:
            task_id:
                Task identificator, this is number from 1 to ...
        """

        # Initialize database connection
        db = Database(config["database"]["name"])

        db.execute_query(f"""
DELETE FROM tasks
WHERE id = ?
""", (task_id,))

        db.close()

    def get_all_tasks(self) -> list:
        """
        Reads all tasks from table

        Returns:
            List of tasks, including ID and name
        """

        # Initialize database connection
        db = Database(config["database"]["name"])
        tasks = db.fetch_all("SELECT * FROM tasks")
        db.close()

        return tasks

    async def show_tasks(self, message: Message) -> None:
        tasks = self.get_all_tasks()

        result_string = "Список задач:\n"
        i = 1
        for task in tasks:
            task_name = task[1]
            result_string += f"{i}. {task_name}\n"

            i += 1

        await message.answer(result_string)
