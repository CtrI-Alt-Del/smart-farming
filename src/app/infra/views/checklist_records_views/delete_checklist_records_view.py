from flask import request, render_template

from core.use_cases.checklist_records import (
    delete_checklist_records,
    get_checklist_records_table_page_data,
)
from core.commons import Error
from core.constants import PAGINATION


def delete_checklist_records_view():
    checklist_records_ids = request.form.getlist("checklist-records-ids[]")

    start_date = request.args.get("start-date", None)
    end_date = request.args.get("end-date", None)
    plant_id = request.args.get("plant", "all")
    page_number = int(request.args.get("page", 1))

    try:
        delete_checklist_records.execute(checklist_records_ids)

        data = get_checklist_records_table_page_data.execute(
            page_number=page_number,
            start_date=start_date,
            end_date=end_date,
            plant_id=plant_id,
            should_get_plants=False,
        )

        checklist_records = data["checklist_records"]
        last_page_number = data["last_page_number"]
        current_page_number = data["current_page_number"]

        return render_template(
            "pages/checklist_records_table/records.html",
            checklist_records=checklist_records,
            last_page_number=last_page_number,
            current_page_number=current_page_number,
            page_buttons_limit=PAGINATION["page_buttons_siblings_count"],
        )
    except Error as error:
        return "ERROR", error.status_code
