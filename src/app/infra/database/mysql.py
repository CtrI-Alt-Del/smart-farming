from os import getenv
from typing import Union, Dict, List
from datetime import datetime
from subprocess import run as run_command

import mysql.connector

from core.commons import Error

from infra.utils import File
from infra.constants import FOLDERS

MYSQL_DATABASE_USER = getenv("MYSQL_DATABASE_USER")
MYSQL_DATABASE_PASSWORD = getenv("MYSQL_DATABASE_PASSWORD")
MYSQL_DATABASE_NAME = getenv("MYSQL_DATABASE_NAME")
MYSQL_DATABASE_HOST = getenv("MYSQL_DATABASE_HOST")


class MySQL:
    def __init__(self) -> None:
        config = {
            "user": MYSQL_DATABASE_USER,
            "password": MYSQL_DATABASE_PASSWORD,
            "database": MYSQL_DATABASE_NAME,
            "host": MYSQL_DATABASE_HOST,
            "raise_on_warnings": True,
        }

        try:
            self.__connection = mysql.connector.connect(**config)
            self.__database = self.__connection.cursor(dictionary=True)

        except mysql.connector.Error as error:
            raise Error(
                internal_message=f"Failed to create a database connection. Error: {error}",
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
                internal_message=f"Failed to execute a query on the database. Error: {error}",
            ) from error

    def mutate(self, sql: str, params):
        try:
            self.__database.execute(sql, params)
            self.__connection.commit()

        except mysql.connector.Error as error:
            self.__connection.rollback()
            self.__close_connection()

            raise Error(
                internal_message=f"Failed to execute a mutation on the database. Error: {error}",
            ) from error

    def mutate_many(self, sql: str, params):
        try:
            self.__database.executemany(sql, params)
            self.__connection.commit()

        except mysql.connector.Error as error:
            self.__connection.rollback()
            self.__close_connection()

            raise Error(
                internal_message=f"Failed to execute a mutation on the database. Error: {error}",
            ) from error

    def create_backup(self):
        try:
            current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"smart-farming-mysql-database-backup-{current_datetime}.sql"

            backup_file = File(folder=FOLDERS["tmp"], filename=filename)

            command = f"mysqldump -h {MYSQL_DATABASE_HOST} -u {MYSQL_DATABASE_USER} -p{MYSQL_DATABASE_PASSWORD} --no-tablespaces -e {MYSQL_DATABASE_NAME} > {backup_file.path.absolute()}"

            run_command(command, shell=True, check=True)

            backup_file.compress()

            return backup_file
        except Exception as exception:
            raise Error(exception)

    def __close_connection(self):
        self.__connection.close()
        self.__database.close()
