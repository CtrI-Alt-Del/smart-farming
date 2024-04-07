from flask import render_template


def get_checklist_dashboard_page():
    return render_template("/pages/checklist_dashboard.html")
