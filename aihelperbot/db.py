import sqlite3


class Database:
    def __init__(self, database_name: str) -> None:
        # Connecting to database
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def execute_query(self, query: str, data = None) -> list:
        # Executing query
        if data:
            self.cursor.execute(query, (data))
        else:
            self.cursor.execute(query)

        # Saves changes
        self.connection.commit()

        return self.cursor.fetchall()

    def close(self) -> None:
        # Closing database connection
        self.connection.close()
