from flask import render_template


def get_sensors_dashboard_page_view():
    return render_template("/pages/sensors_dashboard.html")
