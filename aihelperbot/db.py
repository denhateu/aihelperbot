import sqlite3


class Database:
    def __init__(self, database_name: str) -> None:
        # Connecting to database
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def execute_query(self, query: str) -> None:
        # Executing query
        self.cursor.execute(query)

        # Saves changes
        self.connection.commit()

    def add_data(self, table_name: str, column_name: str, data) -> None:
        # Executing query
        self.cursor.execute(f"""
INSERT INTO {table_name} ({column_name})
VALUES (?)
""", (data,))

        # Saves changes
        self.connection.commit()

    def get_all_data(self, table_name: str) -> list:
        # Executing query
        self.cursor.execute(f"SELECT * FROM {table_name}")

        # Returns got rows from db
        return self.cursor.fetchall()

    def check_if_data_exists(self, table_name: str, element_id: str) -> bool:
        # Executing query with element ID
        self.cursor.execute(f"SELECT * FROM {table_name} WHERE id = ?", (element_id,))

        result = self.cursor.fetchone()
        if result:
            return True
        else:
            return False

    def close(self) -> None:
        # Closing database connection
        self.connection.close()
