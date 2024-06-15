from flask import Blueprint

from .login_page_view import login_page_view
from .request_password_reset_page_view import request_password_reset_page_view
from .login_user_view import login_user_view
from .logout_user_view import logout_user_view
from .request_password_reset_view import request_password_reset_view
from .reset_password_page_view import reset_password_page_view
from .reset_password_view import reset_password_view

authentication_views = Blueprint("authentication_views", __name__)

route = authentication_views.add_url_rule

route("/login", view_func=login_page_view, methods=["GET"])

route("/login", view_func=login_user_view, methods=["POST"])

route("/logout", view_func=logout_user_view, methods=["GET"])

route(
    "/request_password_reset",
    view_func=request_password_reset_page_view,
    methods=["GET"],
)

route(
    "/request_password_reset",
    view_func=request_password_reset_view,
    methods=["POST"],
)

route(
    "/reset_password",
    view_func=reset_password_page_view,
    methods=["GET"],
)
route(
    "/reset_password",
    view_func=reset_password_view,
    methods=["POST"],
)
