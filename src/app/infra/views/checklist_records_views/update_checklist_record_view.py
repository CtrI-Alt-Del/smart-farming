from flask import request, render_template

from core.use_cases.checklist_records import update_checklist_record
from core.commons import Error

from infra.forms import ChecklistRecordForm


def update_checklist_record_view(id: str):
    print(request.form, flush=True)
    checklist_record_form = ChecklistRecordForm(formdata=request.form)
    print(checklist_record_form.data, flush=True)

    try:
        if not checklist_record_form.validate_on_submit():
            raise Error("Formulário inválido")

        updated_checklist_record = update_checklist_record.execute(
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
                "checklist_record_id": id,
            },
        )

        return render_template(
            "pages/checklist_records_table/row.html",
            checklist_record=updated_checklist_record,
        )
    except Error as error:
        print(checklist_record_form.errors, flush=True)
        return "ERROR", error.status_code
