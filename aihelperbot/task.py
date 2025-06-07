from db import Database
from config_parser import config


class Task:
    def __init__(self) -> None:
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

    def create_task(self, task_name: str) -> None:
        # Initialize database connection
        db = Database(config["database"]["name"])

        db.execute_query(f"""
INSERT INTO tasks (name)
VALUES (?)
""", (task_name,))

        db.close()

    def edit_task(self, task_id: str, task_name: str) -> None:
        # Initialize database connection
        db = Database(config["database"]["name"])

        db.execute_query(f"""
UPDATE tasks
SET name = ?
WHERE id = ?
""", (task_name, task_id))

        db.close()

    def delete_task(self, task_id: str) -> None:
        # Initialize database connection
        db = Database(config["database"]["name"])

        db.execute_query(f"""
DELETE FROM tasks
WHERE id = ?
""", (task_id,))

        db.close()

    def get_all_tasks(self) -> list:
        # Initialize database connection
        db = Database(config["database"]["name"])
        tasks = db.execute_query("SELECT * FROM tasks")
        db.close()

        return tasks
