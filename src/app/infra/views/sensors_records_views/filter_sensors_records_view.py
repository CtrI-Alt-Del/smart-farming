from flask import render_template, request

from core.use_cases.sensors_records import get_sensors_records_table_page_data
from core.commons import Error


def filter_sensors_records_view():
    page_number = request.args.get("page", 1)

    try:
        sensors_records = get_sensors_records_table_page_data.execute(
            page_number=int(page_number), should_get_plants=False
        )[0]

    except Error as error:
        return "500 ERROR PAGE", error.status_code
    
    return render_template(
            "pages/sensors_records_table/records.html",
            sensors_records=sensors_records,
    )
