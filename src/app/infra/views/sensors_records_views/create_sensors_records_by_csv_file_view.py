from flask import request, render_template

from werkzeug.datastructures import ImmutableMultiDict

from core.use_cases.sensors_records import (
    create_sensors_records_by_csv_file,
    get_sensors_records_table_page_data,
)
from core.commons import Error
from core.constants import PAGINATION

from infra.forms.csv_form import CsvForm


def create_sensors_records_by_csv_file_view():
    form_data = request.form.to_dict()
    form_data["csv"] = request.files["csv"]

    csv_form = CsvForm(ImmutableMultiDict(form_data))

    page_number = int(request.args.get("page", 1))

    try:
        if not csv_form.validate_on_submit():
            raise Error(ui_message="Formulário de check-list inválido", status_code=400)

        create_sensors_records_by_csv_file.execute(request.files["csv"])

        data = get_sensors_records_table_page_data.execute(page_number=page_number)

        updated_sensors_records = data["sensors_records"]
        last_page_number = data["last_page_number"]

        return render_template(
            "pages/sensors_records_table/records.html",
            sensors_records=updated_sensors_records,
            last_page_number=last_page_number,
            current_page_number=page_number,
            page_buttons_limit=PAGINATION["page_buttons_siblings_count"],
        )

    except Error as error:
        return (
            "ERROR",
            error.status_code,
        )
