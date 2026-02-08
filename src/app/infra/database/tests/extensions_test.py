from flask import Flask
from pytest import raises

from infra.database import init_database
from infra.database.extensions import get_database_uri


def describe_get_database_uri():
    def it_should_return_in_memory_sqlite_uri_in_test_environment(monkeypatch):
        monkeypatch.setenv("ENVIRONMENT", "test")
        monkeypatch.delenv("MYSQL_DATABASE_USER", raising=False)
        monkeypatch.delenv("MYSQL_DATABASE_PASSWORD", raising=False)
        monkeypatch.delenv("MYSQL_DATABASE_NAME", raising=False)
        monkeypatch.delenv("MYSQL_DATABASE_HOST", raising=False)

        assert get_database_uri() == "sqlite+pysqlite:///:memory:"

    def it_should_build_mysql_uri_when_environment_variables_are_available(monkeypatch):
        monkeypatch.setenv("ENVIRONMENT", "development")
        monkeypatch.setenv("MYSQL_DATABASE_USER", "smart-user")
        monkeypatch.setenv("MYSQL_DATABASE_PASSWORD", "pass with space")
        monkeypatch.setenv("MYSQL_DATABASE_NAME", "smart-farming")
        monkeypatch.setenv("MYSQL_DATABASE_HOST", "localhost")

        assert (
            get_database_uri()
            == "mysql+mysqlconnector://smart-user:pass+with+space@localhost/smart-farming"
        )

    def it_should_raise_when_required_mysql_variables_are_missing(monkeypatch):
        monkeypatch.setenv("ENVIRONMENT", "development")
        monkeypatch.delenv("MYSQL_DATABASE_USER", raising=False)
        monkeypatch.delenv("MYSQL_DATABASE_PASSWORD", raising=False)
        monkeypatch.delenv("MYSQL_DATABASE_NAME", raising=False)
        monkeypatch.delenv("MYSQL_DATABASE_HOST", raising=False)

        with raises(ValueError, match="Missing MySQL environment variables"):
            get_database_uri()


def describe_init_database():
    def it_should_register_sqlalchemy_migrate_and_seed_command(monkeypatch):
        monkeypatch.setenv("ENVIRONMENT", "test")

        app = Flask(__name__)

        init_database(app)

        assert "sqlalchemy" in app.extensions
        assert "migrate" in app.extensions
        assert "db-seed-defaults" in app.cli.commands
