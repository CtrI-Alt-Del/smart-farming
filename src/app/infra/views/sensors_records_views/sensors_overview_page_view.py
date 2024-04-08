from flask import render_template


def get_sensors_overview_page_view():
    return render_template("pages/overview.html")
