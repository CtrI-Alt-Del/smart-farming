from flask import render_template, request

from core.use_cases.sensors_records import update_sensors_records
from core.commons import Error

from infra.forms import SensorsRecordForm

from infra.authentication import auth


@auth.login_middleware
def update_sensors_record_view(id: str):
    sensors_record_form = SensorsRecordForm(request.form)
    try:

        auth_user = auth.get_user()

        if not sensors_record_form.validate_on_submit():
            raise Error("Formulário inválido")

        updated_sensors_record = update_sensors_records.execute(
            {
                "soil_humidity": sensors_record_form.soil_humidity.data,
                "ambient_humidity": sensors_record_form.ambient_humidity.data,
                "temperature": sensors_record_form.temperature.data,
                "water_volume": sensors_record_form.water_volume.data,
                "plant_id": sensors_record_form.plant_id.data,
                "time": sensors_record_form.time.data,
                "date": sensors_record_form.date.data,
                "sensors_record_id": id,
            },
        )

        return render_template(
            "pages/sensors_records_table/row.html",
            sensors_record=updated_sensors_record,
            update_message="Registro atualizado com sucesso",
            auth_user=auth_user,
        )
    except Error as error:
        return (
            render_template(
                "pages/sensors_records_table/update_sensors_record_form/fields.html",
                update_sensors_record_form=sensors_record_form,
                auth_user=auth_user,
            ),
            error.status_code,
        )
