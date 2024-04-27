from flask import render_template

from core.use_cases.sensors_records import get_last_sensors_record


def last_sensors_record_page_view():
    try:
        last_sensors_record = get_last_sensors_record.execute()
    except Exception:
        pass

    return render_template(
        "pages/last_sensors_record/index.html",
        last_sensors_record=last_sensors_record,
        datetime=last_sensors_record.created_at.strftime("%d-%m-%Y %H:%M:%S"),
        #datetime=last_sensors_record.created_at,
    )
