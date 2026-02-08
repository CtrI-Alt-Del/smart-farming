from os import getenv
from typing import cast
from urllib.parse import quote_plus

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate(compare_type=True)


def get_database_uri() -> str:
    if getenv("ENVIRONMENT") == "test":
        return "sqlite+pysqlite:///:memory:"

    mysql_database_user = getenv("MYSQL_DATABASE_USER")
    mysql_database_password = getenv("MYSQL_DATABASE_PASSWORD")
    mysql_database_name = getenv("MYSQL_DATABASE_NAME")
    mysql_database_host = getenv("MYSQL_DATABASE_HOST")

    missing_environment_variables = [
        key
        for key, value in {
            "MYSQL_DATABASE_USER": mysql_database_user,
            "MYSQL_DATABASE_PASSWORD": mysql_database_password,
            "MYSQL_DATABASE_NAME": mysql_database_name,
            "MYSQL_DATABASE_HOST": mysql_database_host,
        }.items()
        if not value
    ]

    if missing_environment_variables:
        missing_variables_str = ", ".join(missing_environment_variables)
        raise ValueError(
            f"Missing MySQL environment variables for SQLAlchemy: {missing_variables_str}"
        )

    assert mysql_database_user is not None
    assert mysql_database_password is not None
    assert mysql_database_name is not None
    assert mysql_database_host is not None

    password = quote_plus(cast(str, mysql_database_password))
    return (
        "mysql+mysqlconnector://"
        f"{mysql_database_user}:{password}@{mysql_database_host}/{mysql_database_name}"
    )


def init_database_extensions(app: Flask) -> None:
    if "SQLALCHEMY_DATABASE_URI" not in app.config:
        app.config["SQLALCHEMY_DATABASE_URI"] = get_database_uri()

    app.config.setdefault("SQLALCHEMY_TRACK_MODIFICATIONS", False)

    db.init_app(app)
    migrate.init_app(app, db)
