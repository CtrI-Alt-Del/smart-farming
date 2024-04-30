from flask import redirect, make_response, url_for, flash, request

from core.use_cases.sensors_records import update_sensors_records
from core.commons import Error

from infra.forms import SensorsRecordsForm


def update_sensors_record_view():
    sensors_record_form = SensorsRecordsForm(request.form)

    response = make_response(
        redirect(url_for("sensors_records_views.sensors_records_table_page_view"))
    )

    if sensors_record_form.validate_on_submit():
        try:
            update_sensors_records.execute(
                {
                    "soil_humidity": sensors_record_form.soil_humidity.data,
                    "ambient_humidity": sensors_record_form.ambient_humidity.data,
                    "temperature": sensors_record_form.temperature.data,
                    "water_volume": sensors_record_form.water_volume.data,
                    "plant_id": sensors_record_form.plant_id.data,
                    "date": sensors_record_form.date.data,
                    "sensors_record_id": request.form["id"],
                },
            )

            flash("Registro dos sensores atualizado com sucesso", "success")
            return response
        except Error as error:
            flash(error.ui_message, "error")
            return response

    flash("Registro de sensor inválido", "error")
    return response
