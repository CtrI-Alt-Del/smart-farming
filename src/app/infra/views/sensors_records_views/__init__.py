from flask import Blueprint

from .get_sensors_records_page import get_sensors_records_page_view
from .get_sensors_dashboard_page import get_sensors_dashboard_page_view
from .create_sensors_records_by_csv_view import create_sensors_records_by_csv_view

sensors_records_views = Blueprint("sensors_records_views", __name__)

route = sensors_records_views.add_url_rule

route(rule="/", view_func=get_sensors_dashboard_page_view, methods=["GET"])

route(
    rule="/sensors_records/",
    view_func=get_sensors_records_page_view,
    methods=["GET"],
)

route(
    rule="/sensors_records/csv",
    view_func=create_sensors_records_by_csv_view,
    methods=["POST"],
)
