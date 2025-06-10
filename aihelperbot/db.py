import sqlite3
from typing import Tuple, Any, Optional


class Database:
    """
    This is simple database manager class, this class including methods
    for only execute query, execute query and fetch one record and
    execute query and fetch all records
    """

    def __init__(self, database_name: str) -> None:
        """
        Initialize connection to database and creates cursor object for
        database management

        Args:
            database_name:
                The name of the database to which you want to connect
        """

        # Connecting to database
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def execute_query(self, query: str,
                      params: Optional[Tuple[Any, ...]] = None) -> None:
        """
        Executing SQL query with parameters, but parameters are not
        required

        Args:
            query:
                SQL query string
            params:
                Various data that are needed to fulfill the request
        """

        # Executing query
        self.cursor.execute(query, params or ())

        # Saves changes
        self.connection.commit()

    def fetch_all(self, query: str,
                  params: Optional[Tuple[Any, ...]] = None) -> list:
        """
        Executing SQL query with parameters, but parameters are not
        required

        Args:
            query:
                SQL query string
            params:
                Various data that are needed to fulfill the request

        Returns:
            List of all got elements from table
        """

        # Executing query
        self.cursor.execute(query, params or ())
        return self.cursor.fetchall()

    def fetch_one(self, query: str,
                  params: Optional[Tuple[Any, ...]] = None) -> list:
        """
        Executing SQL query with parameters, but parameters are not
        required

        Args:
            query:
                SQL query string
            params:
                Various data that are needed to fulfill the request

        Returns:
            A list containing the very first element found
        """

        # Executing query
        self.cursor.execute(query, params or ())
        return self.cursor.fetchone()

    def close(self) -> None:
        """
        Closes database connection
        """

        # Closing database connection
        self.connection.close()
