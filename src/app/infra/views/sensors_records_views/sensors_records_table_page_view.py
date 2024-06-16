from flask import render_template, request

from core.use_cases.sensors_records import get_sensors_records_table_page_data
from core.commons import Error
from core.constants import PAGINATION

from infra.forms import SensorsRecordForm
from infra.forms import CsvForm

from infra.authentication import auth


def sensors_records_table_page_view():
    auth_user = auth.get_user()
    active_plant_id = (
        auth_user.active_plant_id if hasattr(auth_user, "active_plant_id") else None
    )

    page_number = int(request.args.get("page", 1))
    start_date = request.args.get("start-date", None)
    end_date = request.args.get("end-date", None)
    plant_id = request.args.get("plant", "all")

    create_sensors_record_form = SensorsRecordForm(active_plant_id=active_plant_id)
    update_sensors_record_form = SensorsRecordForm(active_plant_id=active_plant_id)

    csv_form = CsvForm()

    try:
        data = get_sensors_records_table_page_data.execute(
            page_number=page_number,
            start_date=start_date,
            end_date=end_date,
            plant_id=plant_id,
            should_get_plants=True,
        )
        sensors_records = data["sensors_records"]
        plants = data["plants"]
        last_page_number = data["last_page_number"]
        current_page_number = data["current_page_number"]

        return render_template(
            "pages/sensors_records_table/index.html",
            csv_form=csv_form,
            create_sensors_record_form=create_sensors_record_form,
            update_sensors_record_form=update_sensors_record_form,
            sensors_records=sensors_records,
            plants=plants,
            selected_plant_id=plant_id,
            selected_start_date=start_date,
            selected_end_date=end_date,
            last_page_number=last_page_number,
            current_page_number=current_page_number,
            page_buttons_limit=PAGINATION["page_buttons_siblings_count"],
            auth_user=auth_user,
        )

    except Error as error:
        return error, 500
