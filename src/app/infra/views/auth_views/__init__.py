from flask import Blueprint

from .login_page_view import login_page_view

auth_views = Blueprint("auth_views", __name__)

route = auth_views.add_url_rule

route(rule="/login", view_func=login_page_view, methods=["GET"])
