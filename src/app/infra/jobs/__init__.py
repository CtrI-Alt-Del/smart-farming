from flask_apscheduler import APScheduler

from .create_database_backup_job import create_database_backup_job


def init_jobs():
    scheduler = APScheduler()

    scheduler.add_job(
        func=create_database_backup_job,
        trigger="interval",
        days=1,
        id="Create Database Backup Job",
    )

    scheduler.start()
