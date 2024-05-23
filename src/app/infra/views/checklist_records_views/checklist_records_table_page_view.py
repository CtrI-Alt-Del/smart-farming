from flask import render_template, request

from core.use_cases.checklist_records import get_checklist_records_table_page_data
from core.commons import Error
from core.constants import PAGINATION

from infra.forms import ChecklistRecordForm, CsvForm


def checklist_records_table_page_view():
    start_date = request.args.get("start-date", None)
    end_date = request.args.get("end-date", None)
    plant_id = request.args.get("plant", "all")
    page_number = int(request.args.get("page", 1))

    create_checklist_record_form = ChecklistRecordForm()
    csv_form = CsvForm()

    try:
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
        )
    except Error as error:
        print(error, flush=True)
        return "500 ERROR PAGE"
