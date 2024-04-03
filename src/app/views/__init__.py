from .sensors_views import sensors_views
from .checklist_views import checklist_views

def init_views(app):
    app.register_blueprint(sensors_views)
    app.register_blueprint(checklist_views)
