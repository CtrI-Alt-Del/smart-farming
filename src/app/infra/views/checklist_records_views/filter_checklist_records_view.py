from flask import render_template, request

from core.use_cases.checklist_records import get_checklist_records_table_page_data
from core.commons import Error


def filter_checklist_records_view():
    page_number = request.args.get("page", 1)

    try:
        checklist_records = get_checklist_records_table_page_data.execute(
            page_number=int(page_number), should_get_plants=False
        )[0]

        print(len(checklist_records), flush=True)

        return render_template(
            "pages/checklist_records_table/records.html",
            checklist_records=checklist_records,
        )
    except Error:
        return "500 ERROR PAGE"
