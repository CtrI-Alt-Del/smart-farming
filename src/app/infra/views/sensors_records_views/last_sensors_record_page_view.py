from flask import render_template

from core.use_cases.sensors_records import get_last_record

def last_sensors_record_page_view():
    last_data = get_last_record.execute()

    if last_data:
        last_data = last_data
        datetime = last_data.created_at.strftime("%d-%m-%Y %H:%M:%S")
        return render_template(
            "pages/last_sensors_record/index.html",
            last_sensors_records=last_data,
            datetime=datetime,
        )
    else:
        return "No data found", 404
