from flask import Blueprint

from .last_sensors_record_page_view import last_sensors_record_page_view
from .sensors_records_dashboard_page_view import sensors_records_dashboard_page_view
from .create_sensors_records_by_csv_file_view import (
    create_sensors_records_by_csv_file_view,
)
from .update_sensors_records_view import update_sensors_record_view
from .update_sensors_record_form_view import update_sensors_record_form_view
from .delete_sensors_records_view import delete_sensors_records_view
from .sensors_records_table_page_view import sensors_records_table_page_view
from .create_sensors_records_by_form_view import create_sensors_record_by_form_view
from .filter_sensors_records_view import filter_sensors_records_view

sensors_records_views = Blueprint("sensors_records_views", __name__)

route = sensors_records_views.add_url_rule

route("/", view_func=last_sensors_record_page_view, methods=["GET"])

route(
    "/sensors_records/dashboard",
    view_func=sensors_records_dashboard_page_view,
    methods=["GET"],
)

route(
    "/sensors_records/table",
    view_func=sensors_records_table_page_view,
    methods=["GET"],
)

route(
    "/sensors_records/<id>/form",
    view_func=update_sensors_record_form_view,
    methods=["GET"],
)

route(
    "/sensors_records/filter",
    view_func=filter_sensors_records_view,
    methods=["GET"],
)

route(
    "/sensors_records/csv",
    view_func=create_sensors_records_by_csv_file_view,
    methods=["POST"],
)

route(
    "/sensors_records/form",
    view_func=create_sensors_record_by_form_view,
    methods=["POST"],
)

route("/sensors_records/<id>", view_func=update_sensors_record_view, methods=["PUT"])

route(
    "/sensors_records",
    view_func=delete_sensors_records_view,
    methods=["DELETE"],
)
