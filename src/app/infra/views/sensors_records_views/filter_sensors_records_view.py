from flask import render_template, request

from core.use_cases.sensors_records import get_sensors_records_table_page_data
from core.commons import Error
from core.constants import PAGINATION


def filter_sensors_records_view():
    start_date = request.args.get("start-date", None)
    end_date = request.args.get("end-date", None)
    plant_id = request.args.get("plant", "all")
    page_number = int(request.args.get("page", 1))

    try:
        data = get_sensors_records_table_page_data.execute(
            page_number=page_number,
            start_date=start_date,
            end_date=end_date,
            plant_id=plant_id,
            should_get_plants=False,
        )

        filtered_sensors_records = data["sensors_records"]
        last_page_number = data["last_page_number"]
        current_page_number = data["current_page_number"]

        return render_template(
            "pages/sensors_records_table/records.html",
            sensors_records=filtered_sensors_records,
            last_page_number=last_page_number,
            current_page_number=current_page_number,
            page_buttons_limit=PAGINATION["page_buttons_siblings_count"],
        )

    except Error as error:
        return "ERROR", error.status_code  ##sla pq é assim mas o petros fez assim
