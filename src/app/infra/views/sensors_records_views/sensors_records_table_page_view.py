from flask import render_template, request

from core.use_cases.sensors_records import get_sensors_records_table_page_data
from core.commons import Error
from core.constants import PAGINATION

from infra.forms import SensorsRecordsForm
from infra.forms import CsvForm


def sensors_records_table_page_view():
    page_number = int(request.args.get("page", 1))

    create_sensors_records_form = SensorsRecordsForm()
    update_sensors_records_form = SensorsRecordsForm()

    csv_form = CsvForm()
    try:
        data = get_sensors_records_table_page_data.execute(
            page_number=page_number, should_get_plants=True
        )

        sensors_records = data["sensors_records"]
        plants = data["plants"]
        last_page_number = data["last_page_number"]

        return render_template(
            "pages/sensors_records_table/index.html",
            csv_form=csv_form,
            create_sensors_records_form=create_sensors_records_form,
            update_sensors_records_form=update_sensors_records_form,
            sensors_records=sensors_records,
            plants=plants,
            last_page_number=last_page_number,
            current_page_number=page_number,
            page_buttons_limit=PAGINATION["page_buttons_siblings_count"],
        )
    except Error:
        return "500 ERROR PAGE"
