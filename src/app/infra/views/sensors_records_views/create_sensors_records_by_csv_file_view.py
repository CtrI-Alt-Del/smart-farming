from flask import request, redirect, url_for

from werkzeug.datastructures import ImmutableMultiDict

from core.use_cases.sensors_records import create_sensors_records_by_csv_file
from core.commons.error import Error

from infra.forms.csv_form import CsvForm


def create_sensors_records_by_csv_file_view():
    form_data = request.form.to_dict()
    form_data["csv"] = request.files["csv"]

    csv_form = CsvForm(ImmutableMultiDict(form_data))

    try:
        if csv_form.validate_on_submit():
            create_sensors_records_by_csv_file.execute(request.files["csv"])
    except Error as error:
        print("ui_message", error.ui_message, flush=True)
        return redirect(
            url_for("sensors_records_views.sensors_records_table_page_view")
        )

    return redirect(
        url_for("sensors_records_views.sensors_records_dashboard_page_view")
    )
