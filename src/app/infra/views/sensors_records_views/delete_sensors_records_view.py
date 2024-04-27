from flask import redirect, url_for, make_response, flash, request

from core.use_cases.sensors_records import delete_sensors_records
from core.commons import Error

def delete_sensors_records_view():
    response = make_response(
        redirect(url_for("sensors_records_views.sensors_records_table_page_view")),
    )
    
    sensors_records_ids = request.form.getlist("sensors_records_ids[]")
    
    try:
        delete_sensors_records.execute(sensors_records_ids)
        
        flash("Registro(s) dos sensores deletado(s) com sucesso", "success")
        return response
    except Error as error:
        flash(error.ui_message, "error")
        return response

    