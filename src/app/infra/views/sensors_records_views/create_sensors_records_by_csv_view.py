from flask import request

from werkzeug.datastructures import ImmutableMultiDict

from infra.forms.csv_form import CsvForm
from core.use_cases.sensors_records import create_sensors_by_csv_file


def create_sensors_records_by_csv_view():
    form_data = request.form.to_dict()
    form_data["csv"] = request.files["csv"]

    print(form_data["csv"], flush=True)
    create_sensors_by_csv_file.execute(request.files["csv"])
    return "CSV"
