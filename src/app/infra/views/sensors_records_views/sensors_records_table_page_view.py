from flask import render_template, request

from infra.forms import CsvForm
from core.use_cases.sensors_records import get_sensors_records_table_page_data

from infra.forms import SensorsRecordsForm

from core.commons import Error


def sensors_records_table_page_view():
    page_number = request.args.get("page", 0)

    create_sensors_records_form = SensorsRecordsForm()

    csv_form = CsvForm()
    try:
        plants, sensors_records = get_sensors_records_table_page_data.execute(
            page_number=page_number
        )

        print(plants, flush=True)
        return render_template(
            "pages/sensors_records_table/index.html",
            csv_form=csv_form,
            sensors_records_form=create_sensors_records_form,
            sensors_records=sensors_records,
            plants=plants,
        )
    except Error:
        return "500 ERROR PAGE"
