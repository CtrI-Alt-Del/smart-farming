from flask import Blueprint

from .plants_page_view import plants_page_view

plants_views = Blueprint("plants_views", __name__)

route = plants_views.add_url_rule

route(rule="/plants", view_func=plants_page_view, methods=["GET"])
