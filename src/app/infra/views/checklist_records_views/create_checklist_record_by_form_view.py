from flask import redirect, url_for, flash, request

from core.use_cases.checklist_records import create_checklist_record_by_form
from core.commons.error import Error

from infra.forms.checklist_record_form import ChecklistRecordForm


def create_checklist_record_by_form_view():
    checklist_record_form = ChecklistRecordForm(request.form)

    if checklist_record_form.validate_on_submit():
        try:
            create_checklist_record_by_form.execute(
                {
                    "fertilizer_expiration_date": checklist_record_form.fertilizer_expiration_date.data,
                    "illuminance": checklist_record_form.illuminance.data,
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
                    "plant_id": checklist_record_form.plant_id.data,
                }
            )

            flash("Registro check-list salvo com sucesso", "success")
            return redirect_to_checklist_records_table_page_view(201)
        except Error as error:
            flash(error.ui_message, "error")
            return redirect_to_checklist_records_table_page_view(error.status_code)

    flash("Registro de check-list inválido", "error")
    return redirect_to_checklist_records_table_page_view(401)


def redirect_to_checklist_records_table_page_view(status_code: int):
    return redirect(
        url_for("checklist_records_views.checklist_records_table_page_view")
    ), status_code
