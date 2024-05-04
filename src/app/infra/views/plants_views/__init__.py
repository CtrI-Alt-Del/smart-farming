from flask import Blueprint

from .plants_page_view import plants_page_view
from .create_plant_by_form_view import create_plant_by_form_view

plants_views = Blueprint("plants_views", __name__)

route = plants_views.add_url_rule

route("/plants", view_func=plants_page_view, methods=["GET"])

route("/plants/<id>/form", view_func=plants_page_view, methods=["GET"])

route("/plants/form", view_func=create_plant_by_form_view, methods=["POST"])

route("/plants/<id>", view_func=create_plant_by_form_view, methods=["PUT"])
