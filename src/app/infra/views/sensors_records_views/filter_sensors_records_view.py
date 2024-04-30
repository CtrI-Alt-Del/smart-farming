from flask import render_template, request

from core.use_cases.sensors_records import get_sensors_records_table_page_data
from core.commons import Error
from core.constants import PAGINATION


def filter_sensors_records_view():
    page_number = int(request.args.get("page", 1))

    try:
        data = get_sensors_records_table_page_data.execute(
            page_number=int(page_number), should_get_plants=False
        )

        filtered_sensors_records = data["sensors_records"]
        last_page_number = data["last_page_number"]

    except Error as error:
        return "ERROR", error.status_code

    return render_template(
        "pages/sensors_records_table/records.html",
        sensors_records=filtered_sensors_records,
        last_page_number=last_page_number,
        current_page_number=page_number,
        page_buttons_limit=PAGINATION["page_buttons_siblings_count"],
    )
