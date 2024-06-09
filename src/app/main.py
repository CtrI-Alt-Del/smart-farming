from os import getenv

from flask import Flask

from infra.database import init_database
from infra.jobs import init_jobs
from infra.authentication import init_authentication
from infra.views import init_views


def init_app():
    app = Flask(
        __name__, template_folder="../ui/templates", static_folder="../ui/static"
    )

    app.config["SECRET_KEY"] = getenv("SECRET_KEY")

    init_database()
    init_jobs()
    init_authentication(app)
    init_views(app)

    return app
