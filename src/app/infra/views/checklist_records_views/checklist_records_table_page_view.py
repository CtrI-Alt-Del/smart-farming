from flask import render_template


def checklist_records_table_page_view():
    return render_template("/pages/checklist_records/dashboard/index.html")
