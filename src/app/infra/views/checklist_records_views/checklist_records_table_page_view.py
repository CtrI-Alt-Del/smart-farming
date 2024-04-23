from flask import render_template

from infra.forms.checklist_record_form import ChecklistRecordForm


def checklist_records_table_page_view():
    checklist_record_form = ChecklistRecordForm()

    return render_template(
        "/pages/checklist_records_table/index.html",
        checklist_record_form=checklist_record_form,
    )
