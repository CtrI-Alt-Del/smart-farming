from flask import render_template

from core.use_cases.checklist_records import get_checklist_records_dashboard_page_data


def checklist_records_dashboard_page_view():
    data = get_checklist_records_dashboard_page_data.execute()

    print(data["leaf_appearances_records_days_count"], flush=True)

    return render_template("pages/checklist_records_dashboard/index.html")
