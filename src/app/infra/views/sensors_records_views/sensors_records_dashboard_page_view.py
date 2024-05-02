from flask import render_template, redirect, url_for

from core.use_cases.sensors_records import get_sensors_dashboard_page_data
from core.commons import Error


def sensors_records_dashboard_page_view():
    try:
        charts_filtered_data = get_sensors_dashboard_page_data.execute()
    except Error:
        return redirect(
            url_for("sensors_records_views.sensors_records_table_page_view")
        )

    return render_template(
        "pages/sensors_records_dashboard/index.html",
        charts_filtered_data=charts_filtered_data,
    )
