from flask import render_template, request

from infra.factories.use_cases.checklist_records import (
    get_checklist_records_table_page_data,
)
from core.constants import PAGINATION

from infra.forms import ChecklistRecordForm, CsvForm
from infra.authentication import auth


def checklist_records_table_page_view():
    start_date = request.args.get("start-date", None)
    end_date = request.args.get("end-date", None)
    plant_id = request.args.get("plant", "all")
    page_number = int(request.args.get("page", 1))

    try:
        auth_user = auth.get_user()
        active_plant_id = (
            auth_user.active_plant_id if hasattr(auth_user, "active_plant_id") else None
        )

        create_checklist_record_form = ChecklistRecordForm(
            active_plant_id=active_plant_id
        )
        csv_form = CsvForm()

        data = get_checklist_records_table_page_data.execute(
            page_number=page_number,
            start_date=start_date,
            end_date=end_date,
            plant_id=plant_id,
            should_get_plants=True,
        )

        checklist_records = data["checklist_records"]
        plants = data["plants"]
        last_page_number = data["last_page_number"]
        current_page_number = data["current_page_number"]

        return render_template(
            "pages/checklist_records_table/index.html",
            create_checklist_record_form=create_checklist_record_form,
            csv_form=csv_form,
            checklist_records=checklist_records,
            plants=plants,
            selected_plant_id=plant_id,
            selected_start_date=start_date,
            selected_end_date=end_date,
            last_page_number=last_page_number,
            current_page_number=current_page_number,
            page_buttons_limit=PAGINATION["page_buttons_siblings_count"],
            auth_user=auth_user,
        )
    except Exception as error:
        return error.ui_message, error.status_code
