from flask import render_template

from infra.repositories import SensorRecordsRepository



sensors_records_repo = SensorRecordsRepository()


def last_sensors_record_page_view():
    last_data = sensors_records_repo.get_last_record()

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
