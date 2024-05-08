from flask import render_template

from core.use_cases.sensors_records import get_last_sensors_record_page_data
from core.entities import SensorsRecord
from core.commons.error import Error


def last_sensors_record_page_view():
    try:
        data = get_last_sensors_record_page_data.execute()

        variations = data["variations"]
        last_sensors_record = data["last_sensors_record"]
    except Error:
        last_sensors_record = SensorsRecord(
            soil_humidity=0,
            ambient_humidity=0,
            temperature=0,
            water_volume=0,
        )
        variations = {}

    return render_template(
        "pages/last_sensors_record/index.html",
        last_sensors_record=last_sensors_record,
        variations=variations,
        datetime=last_sensors_record.created_at,
    )
