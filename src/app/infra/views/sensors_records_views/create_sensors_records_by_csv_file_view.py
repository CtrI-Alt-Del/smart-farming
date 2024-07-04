from flask import request, render_template

from werkzeug.datastructures import ImmutableMultiDict

from core.errors.validation import CSVFileNotValidError
from core.constants import PAGINATION

from infra.factories.use_cases.sensors_records import (
    create_sensors_records_by_csv_file,
    get_sensors_records_table_page_data,
)
from infra.forms.csv_form import CsvForm
from infra.authentication import auth


@auth.login_middleware
def create_sensors_records_by_csv_file_view():
    form_data = request.form.to_dict()
    form_data["csv"] = request.files["csv"]

    start_date = request.args.get("start-date", None)
    end_date = request.args.get("end-date", None)
    plant_id = request.args.get("plant", "all")
    page_number = int(request.args.get("page", 1))

    csv_form = CsvForm(ImmutableMultiDict(form_data))

    page_number = int(request.args.get("page", 1))

    try:

        auth_user = auth.get_user()

        if not csv_form.validate_on_submit():
            raise CSVFileNotValidError()

        create_sensors_records_by_csv_file.execute(request.files["csv"])

        data = get_sensors_records_table_page_data.execute(
            start_date=start_date,
            end_date=end_date,
            page_number=page_number,
            plant_id=plant_id,
        )

        updated_sensors_records = data["sensors_records"]
        last_page_number = data["last_page_number"]

        return render_template(
            "pages/sensors_records_table/records.html",
            sensors_records=updated_sensors_records,
            last_page_number=last_page_number,
            current_page_number=page_number,
            page_buttons_limit=PAGINATION["page_buttons_siblings_count"],
            create_by_csv_message="Registros dos sensores por arquivo csv realizado com sucesso",
            auth_user=auth_user,
        )

    except Exception as error:
        return (
            render_template(
                "components/csv_form_error.html",
                message=error.ui_message,
                on_load="trigger click on #create-sensors-records-modal-trigger",
                auth_user=auth_user,
            ),
            error.status_code,
        )
