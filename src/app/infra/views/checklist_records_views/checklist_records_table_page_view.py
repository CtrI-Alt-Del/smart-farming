from flask import render_template, request

from core.commons import Error
from core.use_cases.checklist_records import get_checklist_records_table_page_data

from infra.forms import ChecklistRecordForm


def checklist_records_table_page_view():
    page_number = request.args.get("page", 0)

    create_checklist_record_form = ChecklistRecordForm()
    update_checklist_record_form = ChecklistRecordForm()

    try:
        plants, checklist_records = get_checklist_records_table_page_data.execute(
            page_number=page_number
        )

        return render_template(
            "pages/checklist_records_table/index.html",
            create_checklist_record_form=create_checklist_record_form,
            update_checklist_record_form=update_checklist_record_form,
            checklist_records=checklist_records,
            plants=plants,
        )
    except Error:
        return "500 ERROR PAGE"
