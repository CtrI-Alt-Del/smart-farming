from flask import redirect, url_for, make_response, flash, request

from core.use_cases.checklist_records import delete_checklist_records
from core.commons.error import Error


def delete_checklist_records_view():
    response = make_response(
        redirect(url_for("checklist_records_views.checklist_records_table_page_view")),
    )

    checklist_records_ids = request.form.getlist("checklist_records_ids[]")

    try:
        delete_checklist_records.execute(checklist_records_ids)

        flash("Registro(s) check-list deletado(s) com sucesso", "success")
        return response
    except Error as error:
        flash(error.ui_message, "error")
        return response
