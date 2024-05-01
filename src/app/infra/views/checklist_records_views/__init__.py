from flask import Blueprint

from .checklist_records_dashboard_page_view import checklist_records_dashboard_page_view
from .checklist_records_table_page_view import checklist_records_table_page_view
from .create_checklist_record_by_form_view import create_checklist_record_by_form_view
from .create_checklist_records_by_csv_file_view import (
    create_checklist_records_by_csv_file_view,
)
from .filter_checklist_records_view import filter_checklist_records_view
from .update_checklist_record_form_view import update_checklist_record_form_view
from .update_checklist_record_view import update_checklist_record_view
from .delete_checklist_records_view import delete_checklist_records_view

checklist_records_views = Blueprint("checklist_records_views", __name__)

route = checklist_records_views.add_url_rule

route(
    "/checklist_records/dashboard",
    view_func=checklist_records_dashboard_page_view,
    methods=["GET"],
)

route(
    "/checklist_records/table",
    view_func=checklist_records_table_page_view,
    methods=["GET"],
)

route(
    "/checklist_records/filter",
    view_func=filter_checklist_records_view,
    methods=["GET"],
)

route(
    "/checklist_records/<id>/form",
    view_func=update_checklist_record_form_view,
    methods=["GET"],
)

route(
    "/checklist_records/csv",
    view_func=create_checklist_records_by_csv_file_view,
    methods=["POST"],
)

route(
    "/checklist_records/form",
    view_func=create_checklist_record_by_form_view,
    methods=["POST"],
)

route(
    "/checklist_records/<id>",
    view_func=update_checklist_record_view,
    methods=["PUT"],
)

route(
    "/checklist_records",
    view_func=delete_checklist_records_view,
    methods=["DELETE"],
)
