from flask import request

from forms.csv_form import CsvForm
from werkzeug.datastructures import ImmutableMultiDict

from use_cases.sensors_records import create_sensors_by_csv_file


def create_sensors_records_by_csv_view():
    form_data = request.form.to_dict()
    form_data["csv"] = request.files["csv"]

    csv_form = CsvForm(ImmutableMultiDict(form_data))

    print(csv_form.validate_on_submit(), flush=True)
    if csv_form.validate_on_submit():
        create_sensors_by_csv_file.execute(form_data["csv"])

    return "CSV"
