from flask_apscheduler import APScheduler

from .create_database_backup import create_database_backup


def init_jobs():
    scheduler = APScheduler()

    scheduler.add_job(
        func=create_database_backup,
        trigger="interval",
        seconds=5,
        id="Create Database Backup Job",
    )

    scheduler.start()
