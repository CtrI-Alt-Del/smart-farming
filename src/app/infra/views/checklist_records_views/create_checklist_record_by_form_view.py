from flask import redirect, url_for, flash, make_response, request
from json import dumps

from core.use_cases.checklist_records import create_checklist_record_by_form
from core.commons.error import Error

from infra.forms.checklist_record_form import ChecklistRecordForm


def create_checklist_record_by_form_view():
    checklist_record_form = ChecklistRecordForm(request.form)

    response = make_response(
        redirect(url_for("checklist_records_views.checklist_records_table_page_view"))
    )

    print(checklist_record_form.validate_on_submit())
    print(checklist_record_form.data)
    print(checklist_record_form.errors)

    if checklist_record_form.validate_on_submit():
        try:
            create_checklist_record_by_form.execute(
                {
                    "fertilizer_expiration_date": checklist_record_form.fertilizer_expiration_date.data,
                    "illuminance": checklist_record_form.illuminance.data,
                    "plantation_type": checklist_record_form.plantation_type.data,
                    "hour": checklist_record_form.hour.data,
                    "leaf_apperance": checklist_record_form.leaf_apperance.data,
                    "leaf_color": checklist_record_form.leaf_color.data,
                    "air_humidity": checklist_record_form.air_humidity.data,
                    "lai": checklist_record_form.lai.data,
                    "created_at": checklist_record_form.date.data,
                    "report": checklist_record_form.plantation_type.data,
                    "soil_humidity": checklist_record_form.soil_humidity.data,
                    "soil_ph": checklist_record_form.soil_ph.data,
                    "water_consumption": checklist_record_form.water_consumption.data,
                    "temperature": checklist_record_form.temperature.data,
                    "date": checklist_record_form.date.data,
                    "plant_id": checklist_record_form.plant_id.data,
                }
            )

            flash("Registro check-list salvo com sucesso", "success")
            return response
        except Error as error:
            flash(error.ui_message, "error")
            return response

    response.set_cookie(
        "create_checklist_record_form_errors", dumps(checklist_record_form.errors)
    )

    flash("Registro check-list inválido", "error")
    return response
