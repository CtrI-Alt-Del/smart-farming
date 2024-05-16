from datetime import datetime

from flask import render_template, request

from core.use_cases.checklist_records import get_checklist_records_table_page_data
from core.commons import Error, Date
from core.constants import PAGINATION


def filter_checklist_records_view():
    start_date = request.args.get("start-date")
    end_date = request.args.get("end-date")
    plant_id = request.args.get("plant", "all")
    page_number = int(request.args.get("page", 1))

    try:
        print("request", plant_id, flush=True)
        data = get_checklist_records_table_page_data.execute(
            page_number=page_number,
            start_date=Date(start_date).get_value(),
            end_date=Date(end_date).get_value(),
            plant_id=plant_id,
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
        )

    except Error as error:
        return "ERROR", error.status_code
