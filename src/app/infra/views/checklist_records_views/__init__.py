from flask import Blueprint

from .checklist_records_dashboard_page_view import checklist_records_dashboard_page_view
from .checklist_records_table_page_view import checklist_records_table_page_view
from .create_checklist_record_by_form_view import create_checklist_record_by_form_view
from .update_checklist_record_view import update_checklist_record_view
from .delete_checklist_records_view import delete_checklist_records

checklist_records_views = Blueprint("checklist_records_views", __name__)

route = checklist_records_views.add_url_rule

route(
    rule="/checklist_records/dashboard", view_func=checklist_records_dashboard_page_view
)

route(rule="/checklist_records/table", view_func=checklist_records_table_page_view)

route(
    rule="/checklist_records/form",
    view_func=create_checklist_record_by_form_view,
    methods=["POST"],
)

route(
    rule="/checklist_records/update",
    view_func=update_checklist_record_view,
    methods=["POST"],
)

route(
    rule="/checklist_records/delete",
    view_func=delete_checklist_records,
    methods=["POST"],
)
