from json import dumps

from flask import render_template, redirect, url_for, flash

from core.commons import DaysRange

from infra.authentication import auth
from infra.factories.use_cases.sensors_records import (
    get_sensors_records_dashboard_page_data,
)
from infra.utils import JSONEncoder


def sensors_records_dashboard_page_view():
    try:
        auth_user = auth.get_user()

        data = get_sensors_records_dashboard_page_data.execute()

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
        active_plant_id = data["active_plant_id"]
        daysRange = DaysRange()

        return render_template(
            "pages/sensors_records_dashboard/index.html",
            soil_humidity_chart_data=soil_humidity_chart_data,
            ambient_humidity_chart_data=ambient_humidity_chart_data,
            temperature_chart_data=temperature_chart_data,
            water_volume_chart_data=water_volume_chart_data,
            plants=plants,
            active_plant_id=active_plant_id,
            days_ranges=daysRange.get_value(),
            auth_user=auth_user,
        )
    except Exception as error:
        flash(error.ui_message, "error")
        return redirect(
            url_for(
                "plants_views.plants_page_view"
                if "planta" in error.ui_message.lower()
                else "sensors_records_views.sensors_records_table_page_view"
            )
        )
