from flask import render_template

from core.use_cases.sensors_records import get_last_sensors_record
from core.entities import SensorsRecord
from core.commons.error import Error


def last_sensors_record_page_view():
    try:
        last_sensors_record = get_last_sensors_record.execute()
    except Error:
        last_sensors_record = SensorsRecord(
            soil_humidity=0,
            ambient_humidity=0,
            temperature=0,
            water_volume=0,
        )

    return render_template(
        "pages/last_sensors_record/index.html",
        last_sensors_record=last_sensors_record,
        datetime=last_sensors_record.created_at,
    )
