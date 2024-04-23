from flask import render_template

from core.commons.error import Error

from infra.forms.checklist_record_form import ChecklistRecordForm


def checklist_records_table_page_view():
    try:
        checklist_record_form = ChecklistRecordForm()

        return render_template(
            "/pages/checklist_records_table/index.html",
            checklist_record_form=checklist_record_form,
        )
    except Error as error:
        print(error)
        return "500 ERROR PAGE"
