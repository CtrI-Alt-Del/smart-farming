from flask import render_template, request

from infra.forms import CsvForm
from core.use_cases.sensors_records import get_sensors_records_table_page_data

from infra.forms import SensorsRecordsForm

from core.commons import Error


def sensors_records_table_page_view():
    page_number = request.args.get("page", 1)

    create_sensors_records_form = SensorsRecordsForm()
    update_sensors_records_form = SensorsRecordsForm()

    csv_form = CsvForm()
    try:
        sensors_records, pages_count, plants = get_sensors_records_table_page_data.execute(
            page_number=page_number, should_get_plants=True
        )

        return render_template(
            "pages/sensors_records_table/index.html",
            csv_form=csv_form,
            create_sensors_records_form=create_sensors_records_form,
            update_sensors_records_form=update_sensors_records_form,
            sensors_records=sensors_records,
            plants=plants,
            pages_count=pages_count

        )
    except Error:
        return "500 ERROR PAGE"
