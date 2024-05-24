from flask import Blueprint

from .plants_page_view import plants_page_view
from .filter_plants_view import filter_plants_view
from .delete_plant_alert_view import delete_plant_alert_view
from .create_plant_view import create_plant_view
from .update_plant_form_view import update_plant_form_view
from .update_plant_view import update_plant_view
from .delete_plant_view import delete_plant_view

plants_views = Blueprint("plants_views", __name__)

route = plants_views.add_url_rule

route("/plants", view_func=plants_page_view, methods=["GET"])

route("/plants/<id>/form", view_func=update_plant_form_view, methods=["GET"])

route("/plants/filter", view_func=filter_plants_view, methods=["GET"])

route("/plants/<id>/delete-alert", view_func=delete_plant_alert_view, methods=["GET"])

route("/plants/form", view_func=create_plant_view, methods=["POST"])

route("/plants/<id>", view_func=update_plant_view, methods=["PUT"])

route("/plants/<id>", view_func=delete_plant_view, methods=["DELETE"])
