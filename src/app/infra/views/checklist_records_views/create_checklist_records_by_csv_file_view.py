from werkzeug.datastructures import ImmutableMultiDict

from flask import render_template, request

from infra.factories.use_cases.checklist_records import (
    create_checklist_records_by_csv_file,
    get_checklist_records_table_page_data,
)

from core.constants import PAGINATION
from core.errors.validation import ChecklistRecordNotValidError

from infra.forms import CsvForm
from infra.authentication import auth


@auth.login_middleware
def create_checklist_records_by_csv_file_view():

    form_data = request.form.to_dict()
    form_data["csv"] = request.files["csv"]

    csv_form = CsvForm(ImmutableMultiDict(form_data))

    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    plant_id = request.args.get("plant", "all")
    page_number = request.args.get("page", 1)

    try:
        auth_user = auth.get_user()

        if not csv_form.validate_on_submit():
            raise ChecklistRecordNotValidError()

        create_checklist_records_by_csv_file.execute(request.files["csv"])

        data = get_checklist_records_table_page_data.execute(
            page_number=page_number,
            plant_id=plant_id,
            start_date=start_date,
            end_date=end_date,
            should_get_plants=False,
        )

        updated_checklist_records = data["checklist_records"]
        last_page_number = data["last_page_number"]
        current_page_number = data["current_page_number"]

        return render_template(
            "pages/checklist_records_table/records.html",
            checklist_records=updated_checklist_records,
            last_page_number=last_page_number,
            current_page_number=current_page_number,
            page_buttons_limit=PAGINATION["page_buttons_siblings_count"],
            create_by_csv_message="Registros check-list por arquivo csv realizado com sucesso",
            auth_user=auth_user,
        )

    except Exception as error:
        return (
            render_template(
                "components/csv_form_error.html",
                message=error.ui_message,
                on_load="trigger click on #create-checklist-records-modal-trigger",
            ),
            error.status_code,
        )
