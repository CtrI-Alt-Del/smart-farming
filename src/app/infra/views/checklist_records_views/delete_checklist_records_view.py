from flask import request

from core.use_cases.checklist_records import delete_checklist_records
from core.commons import Error


def delete_checklist_records_view():
    checklist_records_ids = request.form.getlist("checklist_records_ids[]")

    try:
        delete_checklist_records.execute(checklist_records_ids)

        return ""
    except Error as error:
        return ""
