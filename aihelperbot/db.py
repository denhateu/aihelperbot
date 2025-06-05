import sqlite3


class Database:
    def __init__(self, database_name: str) -> None:
        # Connecting to database
        self.connection = sqlite3.connect(database_name)

    def execute_query(self, query: str) -> None:
        cursor = self.connection.cursor()

        # Executing query
        cursor.execute(query)

        # Saves changes
        self.connection.commit()

    def close(self) -> None:
        # Closing database connection
        self.connection.close()
