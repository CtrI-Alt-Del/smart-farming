from flask import Blueprint, render_template

sensors_views = Blueprint("sensors_views",  __name__)
route = sensors_views.add_url_rule

def get_sensor_dashboard():
    return render_template("/pages/sensors_dashboard.html")

route(rule="/", view_func=get_sensor_dashboard)