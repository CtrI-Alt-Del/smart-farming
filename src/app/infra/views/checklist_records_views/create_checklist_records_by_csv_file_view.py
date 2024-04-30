from werkzeug.datastructures import ImmutableMultiDict

from flask import render_template, request

from core.use_cases.checklist_records import (
    create_checklist_records_by_csv_file,
    get_checklist_records_table_page_data,
)

from core.commons import Error
from core.constants import PAGINATION

from infra.forms import CsvForm


def create_checklist_records_by_csv_file_view():
    form_data = request.form.to_dict()
    form_data["csv"] = request.files["csv"]

    csv_form = CsvForm(ImmutableMultiDict(form_data))

    page_number = int(request.args.get("page", 1))

    try:
        if not csv_form.validate_on_submit():
            raise Error(ui_message="Formulário de check-list inválido", status_code=400)

        create_checklist_records_by_csv_file.execute(request.files["csv"])

        data = get_checklist_records_table_page_data.execute(page_number=page_number)

        updated_checklist_records = data["checklist_records"]
        last_page_number = data["last_page_number"]

        return render_template(
            "pages/checklist_records_table/records.html",
            checklist_records=updated_checklist_records,
            last_page_number=last_page_number,
            current_page_number=page_number,
            page_buttons_limit=PAGINATION["page_buttons_siblings_count"],
        )

    except Error as error:
        return (
            "ERROR",
            error.status_code,
        )
