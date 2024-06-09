from time import sleep

from core.commons import Error

from infra.database import mysql
from infra.providers import CloundStorageProvider


def create_database_backup_job():
    try:
        backup_file = mysql.create_backup()
        print("Backup file is successfully created", flush=True)

        clound_storage_provider = CloundStorageProvider()
        clound_storage_provider.create_file(
            file_path=backup_file.path.absolute(),
            filename=backup_file.path.name,
            mimetype="application/gzip",
        )
        print("Backup file is successfully stored on clound", flush=True)

        sleep(1)
        backup_file.delete()

    except Error as error:
        print(f"Create Database Backup Job Error: {error}")
