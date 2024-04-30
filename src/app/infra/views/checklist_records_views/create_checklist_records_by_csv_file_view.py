from werkzeug.datastructures import ImmutableMultiDict

from flask import render_template, request

from core.use_cases.checklist_records import (
    create_checklist_records_by_csv_file,
    get_checklist_records_table_page_data,
)

from core.commons import Error

from infra.forms import CsvForm


def create_checklist_records_by_csv_file_view():
    form_data = request.form.to_dict()
    form_data["csv"] = request.files["csv"]

    csv_form = CsvForm(ImmutableMultiDict(form_data))

    page_number = request.args.get("page", 1)

    print(page_number, flush=True)
    try:
        if not csv_form.validate_on_submit():
            raise Error(ui_message="Formulário de check-list inválido", status_code=400)

        create_checklist_records_by_csv_file.execute(request.files["csv"])
        updated_checklist_records = get_checklist_records_table_page_data.execute(
            page_number=page_number
        )[0]
    except Error as error:
        return (
            render_template(
                "pages/checklist_records_table/records.html",
                checklist_records=[],
            ),
            error.status_code,
        )

    return render_template(
        "pages/checklist_records_table/records.html",
        checklist_records=updated_checklist_records,
    )
