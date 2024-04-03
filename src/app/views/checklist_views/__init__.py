from flask import Blueprint, render_template

checklist_views = Blueprint("checklist_views",  __name__)
route = checklist_views.add_url_rule

def get_sensor_dashboard(id):
    return render_template("/pages/checklist_dashboard.html")

route(rule="/", view_func=get_sensor_dashboard)