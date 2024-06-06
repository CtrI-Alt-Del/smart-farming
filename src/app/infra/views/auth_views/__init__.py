from flask import Blueprint

from .login_page_view import login_page_view
from .request_password_view import request_password_view
from .reset_password_view import reset_password_view

auth_views = Blueprint("auth_views", __name__)

route = auth_views.add_url_rule

route(rule="/login", view_func=login_page_view, methods=["GET"])
route(rule="/request_password", view_func=request_password_view, methods=["GET"])
route(rule="/reset_password", view_func=reset_password_view, methods=["GET"])