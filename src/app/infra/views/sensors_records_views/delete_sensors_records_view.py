from flask import request, render_template

from core.use_cases.sensors_records import (
    delete_sensors_records,
    get_sensors_records_table_page_data,
)
from core.commons import Error
from core.constants import PAGINATION


def delete_sensors_records_view():
    sensors_records_ids = request.form.getlist("sensors-records-ids[]")

    start_date = request.args.get("start-date", None)
    end_date = request.args.get("end-date", None)
    plant_id = request.args.get("plant", "all")
    page_number = int(request.args.get("page", 1))

    try:
        delete_sensors_records.execute(sensors_records_ids)
        data = get_sensors_records_table_page_data.execute(
            start_date=start_date,
            end_date=end_date,
            plant_id=plant_id,
            page_number=page_number,
        )

        sensors_records = data["sensors_records"]
        last_page_number = data["last_page_number"]
        current_page_number = data["current_page_number"]

        return render_template(
            "pages/sensors_records_table/records.html",
            sensors_records=sensors_records,
            last_page_number=last_page_number,
            current_page_number=current_page_number,
            page_buttons_limit=PAGINATION["page_buttons_siblings_count"],
        )
    except Error as error:
        return "ERROR", error.status_code
