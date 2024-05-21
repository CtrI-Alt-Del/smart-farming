from flask import render_template, request

from core.use_cases.sensors_records import (
    create_sensors_records_by_form,
    get_sensors_records_table_page_data,
)
from core.commons import Error
from core.constants import PAGINATION

from infra.forms import SensorsRecordForm


def create_sensors_record_by_form_view():
    sensors_record_form = SensorsRecordForm(request.form)

    start_date = request.args.get("start-date", None)
    end_date = request.args.get("end-date", None)
    plant_id = request.args.get("plant", "all")
    page_number = int(request.args.get("page", 1))

    try:
        if not sensors_record_form.validate_on_submit():
            raise Error("Formulário inválido")

        create_sensors_records_by_form.execute(
            {
                "soil_humidity": sensors_record_form.soil_humidity.data,
                "ambient_humidity": sensors_record_form.ambient_humidity.data,
                "temperature": sensors_record_form.temperature.data,
                "water_volume": sensors_record_form.water_volume.data,
                "plant_id": sensors_record_form.plant_id.data,
                "created_at": sensors_record_form.date.data,
                "date": sensors_record_form.date.data,
                "time": sensors_record_form.time.data,
            }
        )

        data = get_sensors_records_table_page_data.execute(
            start_date=start_date,
            end_date=end_date,
            plant_id=plant_id,
            page_number=page_number,
        )

        updated_sensors_records = data["sensors_records"]
        plants = data["plants"]
        last_page_number = data["last_page_number"]

        return render_template(
            "pages/sensors_records_table/records.html",
            sensors_records=updated_sensors_records,
            plants=plants,
            last_page_number=last_page_number,
            current_page_number=page_number,
            page_buttons_limit=PAGINATION["page_buttons_siblings_count"],
        )
    except Error as error:
        return "ERROR", error.status_code
