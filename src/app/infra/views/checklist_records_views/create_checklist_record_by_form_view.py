from flask import render_template, request

from core.use_cases.checklist_records import (
    create_checklist_record_by_form,
    get_checklist_records_table_page_data,
)
from core.commons import Error
from core.constants import PAGINATION

from infra.forms import ChecklistRecordForm
from infra.forms import CsvForm


def create_checklist_record_by_form_view():
    checklist_record_form = ChecklistRecordForm(request.form)

    start_date = request.args.get("start-date", None)
    end_date = request.args.get("end-date", None)
    plant_id = request.args.get("plant", "all")
    page_number = int(request.args.get("page", 1))

    try:
        if not checklist_record_form.validate_on_submit():
            raise Error

        create_checklist_record_by_form.execute(
            {
                "fertilizer_expiration_date": checklist_record_form.fertilizer_expiration_date.data,
                "illuminance": checklist_record_form.illuminance.data,
                "plantation_type": checklist_record_form.plantation_type.data,
                "time": checklist_record_form.time.data,
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
            }
        )

        data = get_checklist_records_table_page_data.execute(
            page_number=page_number,
            start_date=start_date,
            end_date=end_date,
            plant_id=plant_id,
            should_get_plants=False,
        )

        updated_checklist_records = data["checklist_records"]
        last_page_number = data["last_page_number"]
        current_page_number = data["current_page_number"]

        return render_template(
            "pages/checklist_records_table/records.html",
            message="Registro check-list criado com sucesso",
            checklist_records=updated_checklist_records,
            last_page_number=last_page_number,
            current_page_number=current_page_number,
            page_buttons_limit=PAGINATION["page_buttons_siblings_count"],
        )

    except Error as error:
        render_template(
            "pages/checklist_records_table/create_checklist_record_form/fields.html",
            checklist_record_form=checklist_record_form,
        )

        return (
            render_template(
                "pages/checklist_records_table/create_checklist_record_form/fields.html",
                create_checklist_record_form=checklist_record_form,
                csv_form=csv_form,
                checklist_record=checklist_record_form,
                error_message=error.ui_message,
            ),
            error.status_code,
        )
