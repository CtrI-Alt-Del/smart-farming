from flask import request, render_template

from core.use_cases.checklist_records import update_checklist_record
from core.commons import Error

from infra.forms import ChecklistRecordForm

from infra.authentication import auth


@auth.login_middleware
def update_checklist_record_view(id: str):
    checklist_record_form = ChecklistRecordForm(formdata=request.form)

    try:

        auth_user = auth.get_user()

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
                "report": checklist_record_form.report.data,
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
            update_message="Registro check-list atualizado com sucesso",
            auth_user=auth_user,
        )
    except Error as error:
        print(checklist_record_form.errors, flush=True)
        return (
            render_template(
                "/pages/checklist_records_table/update_checklist_record_form/fields.html",
                update_checklist_record_form=checklist_record_form,
                auth_user=auth_user,
            ),
            error.status_code,
        )
