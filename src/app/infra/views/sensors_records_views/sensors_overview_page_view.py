from flask import render_template

from core.use_cases.sensors_records import get_sensors_dashboard_page_data


def sensors_overview_page_view():
    charts_filtered_data = get_sensors_dashboard_page_data.execute()

    return render_template(
        "pages/sensors_records_overview/index.html", charts_filtered_data
    )
