from flask import redirect, url_for, make_response, flash, request

from core.use_cases.checklist_records import delete_checklist_records
from core.commons import Error


def delete_checklist_records_view():
    checklist_records_ids = request.form.getlist("checklist_records_ids[]")

    print(checklist_records_ids, flush=True)

    try:
        delete_checklist_records.execute(checklist_records_ids)
        return "DELETADO"
    except Error as error:
        return "ERROR", error.status_code
