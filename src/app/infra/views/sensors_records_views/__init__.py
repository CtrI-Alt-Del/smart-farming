from flask import Blueprint

from .sensors_overview_page_view import sensors_overview_page_view
from .sensors_records_dashboard_page import sensors_records_dashboard_page_view
from .create_sensors_records_by_csv_view import create_sensors_records_by_csv_view
from .sensors_records_table_page_view import sensors_records_table_page_view


sensors_records_views = Blueprint("sensors_records_views", __name__)

route = sensors_records_views.add_url_rule

route(rule="/", view_func=sensors_overview_page_view, methods=["GET"])

route(
    rule="/sensors_records/dashboard",
    view_func=sensors_records_dashboard_page_view,
    methods=["GET"],
)

route(
    rule="/sensors_records/table",
    view_func=sensors_records_table_page_view,
    methods=["GET"],
)

route(
    rule="/sensors_records/csv",
    view_func=create_sensors_records_by_csv_view,
    methods=["POST"],
)
