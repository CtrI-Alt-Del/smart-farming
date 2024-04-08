from flask import render_template

from infra.forms.csv_form import CsvForm


def sensors_records_page_view():
    csv_form = CsvForm()

    return render_template("pages/sensors_records.html", csv_form=csv_form)
