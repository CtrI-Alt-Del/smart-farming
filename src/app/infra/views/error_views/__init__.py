from flask import Blueprint

from .error_page_view import error_page_view

error_views = Blueprint("error_page_view", __name__)

route = error_views.add_url_rule

route(rule="/login", view_func=error_page_view, methods=["GET"])

route(
    "/error_page_view/error",
    view_func=error_page_view,
    methods=["GET"],
)
