from flask import render_template, request

from core.use_cases.checklist_records import get_checklist_records_table_page_data
from core.commons import Error
from core.constants import PAGINATION

from infra.forms import ChecklistRecordForm, CsvForm


def checklist_records_table_page_view():
    page_number = int(request.args.get("page", 1))

    create_checklist_record_form = ChecklistRecordForm()
    csv_form = CsvForm()

    try:
        data = get_checklist_records_table_page_data.execute(
            page_number=page_number, should_get_plants=True
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
            last_page_number=last_page_number,
            current_page_number=current_page_number,
            page_buttons_limit=PAGINATION["page_buttons_siblings_count"],
        )
    except Error:
        return "500 ERROR PAGE"
