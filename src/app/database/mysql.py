from os import getenv
from typing import Union, Dict, List

import mysql.connector

from utils.error import Error


class MySQL:
    def __init__(self) -> None:
        config = {
            "user": getenv("MYSQL_DATABASE_USER"),
            "password": getenv("MYSQL_DATABASE_PASSWORD"),
            "database": getenv("MYSQL_DATABASE_NAME"),
            "host": getenv("MYSQL_DATABASE_HOST"),
            "raise_on_warnings": True,
        }

        try:
            self.__connection = mysql.connector.connect(**config)
            self.__database = self.__connection.cursor(dictionary=True)

        except mysql.connector.Error as error:
            raise Error(
                f"Failed to create a database connection. Error: {error}",
                should_abort=False,
            ) from error

    def query(self, sql: str, params: List = None, is_single=True) -> Union[Dict, None]:
        try:
            self.__database.execute(sql, params=params if params is not None else [])

            if is_single:
                return self.__database.fetchone()

            return self.__database.fetchall()

        except mysql.connector.Error as error:
            self.__close_connection()

            raise Error(
                f"Failed to execute a query on the database. Error: {error}",
            ) from error

    def mutate(self, sql: str, params) -> Dict:
        try:
            self.__database.execute(sql, params)
            self.__connection.commit()

        except mysql.connector.Error as error:
            self.__connection.rollback()
            self.__close_connection()

            raise Error(
                f"Failed to execute a mutation on the database. Error: {error}",
            ) from error

    def __close_connection(self):
        self.__connection.close()
        self.__database.close()
