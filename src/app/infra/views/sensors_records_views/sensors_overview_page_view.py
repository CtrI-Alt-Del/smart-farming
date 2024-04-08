from flask import render_template


def sensors_overview_page_view():
    return render_template("pages/sensors_records_overview/index.html")
