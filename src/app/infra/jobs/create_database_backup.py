from core.commons import Error

from infra.database import mysql


def create_database_backup():
    try:
        backup_file = mysql.create_backup()
        print("Backup file successfully created")

    except Error as error:
        print(f"Create Database Backup Job Error: {error}")
