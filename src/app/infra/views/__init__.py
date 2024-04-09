from flask import Flask

from .sensors_records_views import sensors_records_views
from .checklist_records_views import checklist_records_views
from .auth_views import auth_views


def init_views(app: Flask):
    app.register_blueprint(sensors_records_views)
    app.register_blueprint(checklist_records_views)
    app.register_blueprint(auth_views)
