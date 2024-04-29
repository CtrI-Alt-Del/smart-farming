from flask import render_template, request

from core.use_cases.checklist_records import get_checklist_records_table_page_data
from core.commons import Error

from infra.forms import ChecklistRecordForm, CsvForm


def checklist_records_table_page_view():
    page_number = request.args.get("page", 1)

    create_checklist_record_form = ChecklistRecordForm()
    update_checklist_record_form = ChecklistRecordForm()
    csv_form = CsvForm()

    try:
        checklist_records, plants = get_checklist_records_table_page_data.execute(
            page_number=page_number, should_get_plants=True
        )

        return render_template(
            "pages/checklist_records_table/index.html",
            create_checklist_record_form=create_checklist_record_form,
            update_checklist_record_form=update_checklist_record_form,
            csv_form=csv_form,
            checklist_records=checklist_records,
            plants=plants,
        )
    except Error:
        return "500 ERROR PAGE"
