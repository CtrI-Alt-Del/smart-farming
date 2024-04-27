from flask import redirect, make_response, url_for, flash, request

from core.use_cases.checklist_records import update_checklist_record
from core.commons import Error

from infra.forms import ChecklistRecordForm


def update_checklist_record_view():
    checklist_record_form = ChecklistRecordForm(request.form)

    response = make_response(
        redirect(url_for("checklist_records_views.checklist_records_table_page_view"))
    )

    if checklist_record_form.validate_on_submit():
        try:
            print(request.form)
            update_checklist_record.execute(
                {
                    "fertilizer_expiration_date": checklist_record_form.fertilizer_expiration_date.data,
                    "illuminance": checklist_record_form.illuminance.data,
                    "plantation_type": checklist_record_form.plantation_type.data,
                    "hour": checklist_record_form.hour.data,
                    "leaf_appearance": checklist_record_form.leaf_appearance.data,
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
                    "checklist_record_id": request.form["id"],
                },
            )

            flash("Registro check-list atualizado com sucesso", "success")
            return response
        except Error as error:
            flash(error.ui_message, "error")
            return response

    flash("Registro de check-list inválido", "error")
    return response
