from flask import Blueprint

from .login_page_view import login_page_view
from .request_password_reset_page_view import request_password_reset_page_view
from .login_user_view import login_user_view

authentication_views = Blueprint("authentication_views", __name__)

route = authentication_views.add_url_rule

route("/login", view_func=login_page_view, methods=["GET"])

route(
    "/login/request_password_reset",
    view_func=request_password_reset_page_view,
    methods=["GET"],
)

route("/login", view_func=login_user_view, methods=["POST"])
