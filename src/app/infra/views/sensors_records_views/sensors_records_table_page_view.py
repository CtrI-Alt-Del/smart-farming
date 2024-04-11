from flask import render_template

from infra.forms.csv_form import CsvForm


def sensors_records_table_page_view():
    csv_form = CsvForm()

    return render_template("pages/sensors_records_table/index.html", csv_form=csv_form)
