from flask import redirect, url_for, flash, request

from core.use_cases.checklist_records import delete_checklist_records
from core.commons.error import Error


def create_checklist_records_view():
    try:
        delete_checklist_records.execute(request["checklist_records_ids"])

        flash("Registro check-list deletado com sucesso", "success")
        return redirect_to_checklist_records_table_page_view(201)
    except Error as error:
        flash(error.ui_message, "error")
        return redirect_to_checklist_records_table_page_view(error.status_code)


def redirect_to_checklist_records_table_page_view(status_code: int):
    return redirect(
        url_for("checklist_records_views.checklist_records_table_page_view")
    ), status_code
