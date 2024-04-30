from flask import render_template, request

from core.use_cases.checklist_records import get_checklist_records_table_page_data
from core.commons import Error
from core.constants import PAGINATION


def filter_checklist_records_view():
    page_number = int(request.args.get("page", 1))

    try:
        data = get_checklist_records_table_page_data.execute(
            page_number=page_number, should_get_plants=False
        )

        updated_checklist_records = data["checklist_records"]
        last_page_number = data["last_page_number"]

        return render_template(
            "pages/checklist_records_table/records.html",
            checklist_records=updated_checklist_records,
            last_page_number=last_page_number,
            current_page_number=page_number,
            page_buttons_limit=PAGINATION["page_buttons_siblings_count"],
        )

    except Error as error:
        return "ERROR", error.status_code
