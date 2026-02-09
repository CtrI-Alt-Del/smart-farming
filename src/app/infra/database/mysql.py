from os import getenv
from typing import Union, Dict, List
from datetime import datetime
from subprocess import run as run_command

import mysql.connector
from mysql.connector.pooling import MySQLConnectionPool

from core.commons import Error

from infra.utils import File
from infra.constants import FOLDERS

MYSQL_DATABASE_USER = getenv("MYSQL_DATABASE_USER")
MYSQL_DATABASE_PASSWORD = getenv("MYSQL_DATABASE_PASSWORD")
MYSQL_DATABASE_NAME = getenv("MYSQL_DATABASE_NAME")
MYSQL_DATABASE_HOST = getenv("MYSQL_DATABASE_HOST")

ENVIRONMENT = getenv("ENVIRONMENT")

POOL_SIZE = 5


class MySQL:
    def __init__(self) -> None:
        if ENVIRONMENT == "test":
            return

        config = {
            "pool_name": "smart_farming_pool",
            "pool_size": POOL_SIZE,
            "pool_reset_session": True,
            "user": MYSQL_DATABASE_USER,
            "password": MYSQL_DATABASE_PASSWORD,
            "database": MYSQL_DATABASE_NAME,
            "host": MYSQL_DATABASE_HOST,
            "raise_on_warnings": True,
            "autocommit": False,
        }

        try:
            self.__pool = MySQLConnectionPool(**config)

        except mysql.connector.Error as error:
            raise Error(
                internal_message=f"Failed to create a database connection pool. Error: {error}",
            ) from error

    def query(self, sql: str, params: List = None, is_single=True) -> Union[Dict, None]:
        connection = self.__get_connection()

        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute(sql, params=params if params is not None else [])

            if is_single:
                result = cursor.fetchone()
            else:
                result = cursor.fetchall()

            cursor.close()

            return result

        except mysql.connector.Error as error:
            raise Error(
                internal_message=f"Failed to execute a query on the database. Error: {error}",
            ) from error

        finally:
            connection.close()

    def mutate(self, sql: str, params):
        connection = self.__get_connection()

        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute(sql, params)
            connection.commit()
            cursor.close()

        except mysql.connector.Error as error:
            connection.rollback()

            raise Error(
                internal_message=f"Failed to execute a mutation on the database. Error: {error}",
            ) from error

        finally:
            connection.close()

    def mutate_many(self, sql: str, params):
        connection = self.__get_connection()

        try:
            cursor = connection.cursor(dictionary=True)
            cursor.executemany(sql, params)
            connection.commit()
            cursor.close()

        except mysql.connector.Error as error:
            connection.rollback()

            raise Error(
                internal_message=f"Failed to execute a mutation on the database. Error: {error}",
            ) from error

        finally:
            connection.close()

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

    def __get_connection(self):
        try:
            return self.__pool.get_connection()
        except mysql.connector.Error as error:
            raise Error(
                internal_message=f"Failed to get a connection from the pool. Error: {error}",
            ) from error
