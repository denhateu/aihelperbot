import sqlite3
from typing import Tuple, Any, Optional


class Database:
    def __init__(self, database_name: str) -> None:
        # Connecting to database
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def execute_query(self, query: str, params: Optional[Tuple[Any, ...]] = None) -> None:
        # Executing query
        self.cursor.execute(query, params or ())

        # Saves changes
        self.connection.commit()

    def fetch_all(self, query: str, params: Optional[Tuple[Any, ...]] = None) -> list:
        # Executing query
        self.cursor.execute(query, params or ())
        return self.cursor.fetchall()

    def fetch_one(self, query: str, params: Optional[Tuple[Any, ...]] = None) -> list:
        # Executing query
        self.cursor.execute(query, params or ())
        return self.cursor.fetchone()

    def close(self) -> None:
        # Closing database connection
        self.connection.close()
