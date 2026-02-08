from importlib import import_module

import click
from flask import Flask
from sqlalchemy import text

from .mysql import MySQL
from .extensions import db, init_database_extensions

DEFAULT_PLANT_ID = "4544afe3-0661-11ef-9512-0242ac140002"
DEFAULT_PLANT_NAME = "Alface"
DEFAULT_PLANT_HEX_COLOR = "#3A7D44"
DEFAULT_ADMIN_EMAIL = "supsmartfarm@gmail.com"
DEFAULT_ADMIN_PASSWORD_HASH = "$2b$12$GwF4gb7U99hSSEDs6OJr3OenabAd4MEYzGpK4ptavZ14fGwKBVEYy"

mysql = MySQL()


def init_database(app: Flask) -> None:
    import_module("infra.database.models")
    init_database_extensions(app)
    _register_seed_defaults_command(app)


def seed_defaults() -> None:
    with db.engine.begin() as connection:
        connection.execute(
            text(
                """
                INSERT INTO plants (id, name, hex_color)
                SELECT :plant_id, :plant_name, :plant_hex_color
                WHERE NOT EXISTS (
                    SELECT 1 FROM plants WHERE id = :plant_id
                )
                """
            ),
            {
                "plant_id": DEFAULT_PLANT_ID,
                "plant_name": DEFAULT_PLANT_NAME,
                "plant_hex_color": DEFAULT_PLANT_HEX_COLOR,
            },
        )

        connection.execute(
            text(
                """
                INSERT INTO `user` (email, password, active_plant_id)
                SELECT :admin_email, :admin_password_hash, :plant_id
                WHERE NOT EXISTS (
                    SELECT 1 FROM `user` WHERE email = :admin_email
                )
                """
            ),
            {
                "admin_email": DEFAULT_ADMIN_EMAIL,
                "admin_password_hash": DEFAULT_ADMIN_PASSWORD_HASH,
                "plant_id": DEFAULT_PLANT_ID,
            },
        )


def _register_seed_defaults_command(app: Flask) -> None:
    if "db-seed-defaults" in app.cli.commands:
        return

    @app.cli.command("db-seed-defaults")
    def db_seed_defaults_command() -> None:
        """Seed baseline plant and admin user records."""

        seed_defaults()
        click.echo("Default seed data ensured successfully.")
