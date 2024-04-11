from flask import render_template

from core.use_cases.sensors_records import get_sensors_dashboard_page_data


def last_sensors_record_page_view():
    charts_filtered_data = get_sensors_dashboard_page_data.execute()

    return render_template(
        "pages/last_sensors_record/index.html",
        charts_filtered_data=charts_filtered_data,
    )
