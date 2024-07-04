from flask import render_template

from infra.forms import ChecklistRecordForm
from infra.repositories import checklist_records_repository


def update_checklist_record_form_view(id: str):
    try:
        checklist_record = checklist_records_repository.get_checklist_record_by_id(id)

        update_checklist_record_form = ChecklistRecordForm(
            checklist_record=checklist_record
        )

        return render_template(
            "pages/checklist_records_table/update_checklist_record_form/index.html",
            checklist_record_id=checklist_record.id,
            update_checklist_record_form=update_checklist_record_form,
        )
    except Exception as error:
        return "Registro não encontrado 😢", error.status_code
