from flask import Blueprint

from .login_page_view import login_page_view
from .reset_password_view import reset_password_view

auth_views = Blueprint("auth_views", __name__)

route = auth_views.add_url_rule

route(rule="/login", view_func=login_page_view, methods=["GET"])
route(rule="/login/reset_password", view_func=reset_password_view, methods=["GET"])