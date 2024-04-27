from json import dumps

from flask import redirect,url_for,flash,make_response, request


from core.use_cases.sensors_records import create_sensors_records_by_form

from core.commons import Error

from infra.forms import SensorsRecordsForm

def create_sensors_record_by_form_view():
    sensors_record_form = SensorsRecordsForm(request.form)
    
    response = make_response(
        redirect(url_for("sensors_records_views.sensors_records_table_page_view"))   
    )
    print(sensors_record_form.validate_on_submit(),flush=True)
    print(sensors_record_form.errors,flush=True)
    if sensors_record_form.validate_on_submit():
        

        try:
            create_sensors_records_by_form.execute(
                {
                    "soil_humidity": sensors_record_form.soil_humidity.data,
                    "ambient_humidity": sensors_record_form.ambient_humidity.data,
                    "temperature": sensors_record_form.temperature.data,
                    "water_volume": sensors_record_form.water_volume.data,
                    "plant_id": sensors_record_form.plant_id.data,
                    "created_at": sensors_record_form.date.data,
                    "date": sensors_record_form.date.data,
                    "hour": sensors_record_form.hour.data
                }
            )
            flash("Registro dos sensores salvo com sucesso","sucess")
            return response
        except Error as error:
            flash(error.ui_message,"error")
            return response

    response.set_cookie(
        "create_sensors_records_form_errors", dumps(sensors_record_form.errors)
    )
    
    flash("Registro dos sensores inválido","error")
    return response