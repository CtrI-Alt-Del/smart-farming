from flask import Blueprint

from .last_sensors_record_page_view import last_sensors_record_page_view
from .sensors_records_dashboard_page_view import sensors_records_dashboard_page_view
from .create_sensors_records_by_csv_file_view import (
    create_sensors_records_by_csv_file_view,
)
from .sensors_records_table_page_view import sensors_records_table_page_view

from .create_sensors_records_by_form_view import create_sensors_record_by_form_view

sensors_records_views = Blueprint("sensors_records_views", __name__)

route = sensors_records_views.add_url_rule

route(rule="/", view_func=last_sensors_record_page_view, methods=["GET"])

route(
    rule="/sensors_records/dashboard",
    view_func=sensors_records_dashboard_page_view,
    methods=["GET"],
)

route(
    rule="/sensors_records/table",
    view_func=sensors_records_table_page_view,
)

route(
    rule="/sensors_records/csv",
    view_func=create_sensors_records_by_csv_file_view,
    methods=["POST"],
)

route(
    rule="/sensors_records/form",
    view_func=create_sensors_record_by_form_view,
    methods = ["POST"]
)