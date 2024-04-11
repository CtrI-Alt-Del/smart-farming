from flask import Blueprint

from .checklist_records_dashboard_page_view import checklist_records_dashboard_page_view
from .checklist_records_table_page_view import checklist_records_table_page_view

checklist_records_views = Blueprint("checklist_records_views", __name__)
route = checklist_records_views.add_url_rule


route(
    rule="/checklist_records/dashboard", view_func=checklist_records_dashboard_page_view
)

route(rule="/checklist_records/table", view_func=checklist_records_table_page_view)
