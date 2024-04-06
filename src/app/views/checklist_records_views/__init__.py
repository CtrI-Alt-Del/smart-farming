from flask import Blueprint

from .get_checklist_dashboard_page import get_checklist_dashboard_page

checklist_records_views = Blueprint("checklist_records_views", __name__)
route = checklist_records_views.add_url_rule


route(rule="/", view_func=get_checklist_dashboard_page)
