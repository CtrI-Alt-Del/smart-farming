from flask import render_template

from core.use_cases.sensors_records import get_sensors_dashboard_page_data


def get_sensors_dashboard_page_view():
    result = get_sensors_dashboard_page_data.execute()
    return render_template("/pages/sensors_dashboard.html", sensors_record_data=result)
