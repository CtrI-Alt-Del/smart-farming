from flask import Flask
from views import init_views


def init_app():
    app = Flask(
        __name__, template_folder="../ui/templates", static_folder="../ui/static"
    )
    init_views(app)

    return app
