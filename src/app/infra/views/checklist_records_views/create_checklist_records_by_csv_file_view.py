from werkzeug.datastructures import ImmutableMultiDict

from flask import redirect, url_for, request

from core.use_cases.checklist_records import create_checklist_record_by_csv_file

from core.commons import Error

from infra.forms import CsvForm


def create_checklist_records_by_csv_file_view():
    form_data = request.form.to_dict()
    form_data["csv"] = request.files["csv"]

    csv_form = CsvForm(ImmutableMultiDict(form_data))

    try:
        if csv_form.validate_on_submit():
            create_checklist_record_by_csv_file.execute(request.files["csv"])
    except Error:
        return redirect(
            url_for("checklist_records_views.sensors_records_table_page_view")
        )

    return redirect(
        url_for("checklist_records_views.sensors_records_dashboard_page_view")
    )
