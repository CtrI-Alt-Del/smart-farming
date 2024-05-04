from json import dumps

from flask import render_template, redirect, url_for, flash

from core.use_cases.sensors_records import get_sensors_dashboard_page_data
from core.commons import Error, DaysRange

from infra.utils import JSONEncoder


def sensors_records_dashboard_page_view():
    try:
        data = get_sensors_dashboard_page_data.execute()

        soil_humidity_chart_data = dumps(
            data["soil_humidity_chart_data"], cls=JSONEncoder
        )
        ambient_humidity_chart_data = dumps(
            data["ambient_humidity_chart_data"], cls=JSONEncoder
        )
        temperature_chart_data = dumps(data["temperature_chart_data"], cls=JSONEncoder)
        water_volume_chart_data = dumps(
            data["water_volume_chart_data"], cls=JSONEncoder
        )

        plants = data["plants"]
        daysRange = DaysRange()

        return render_template(
            "pages/sensors_records_dashboard/index.html",
            soil_humidity_chart_data=soil_humidity_chart_data,
            ambient_humidity_chart_data=ambient_humidity_chart_data,
            temperature_chart_data=temperature_chart_data,
            water_volume_chart_data=water_volume_chart_data,
            plants=plants,
            days_ranges=daysRange.get_value(),
        )
    except Error as error:
        flash(error.ui_message, "error")
        return redirect(
            url_for(
                "plants_views.plants_page_view"
                if "planta" in error.ui_message.lower()
                else "sensors_records_views.sensors_records_table_page_view"
            )
        )
