from json import dumps
from flask import render_template

from core.use_cases.checklist_records import get_checklist_dashboard_page_data


def checklist_records_dashboard_page_view():
    data = get_checklist_dashboard_page_data.execute()
    leaf_appearences_chart_data = dumps(
        data["days_count_by_leaf_appearance_and_plant"], ensure_ascii=False
    )
    leaf_colors_chart_data = dumps(
        data["days_count_by_leaf_color_and_plant"], ensure_ascii=False
    )
    plants = dumps(data["plants"], ensure_ascii=False)
    
    plant_growth_data = get_checklist_dashboard_page_data.get_plant_growth_chart_data()
    
    


    return render_template(
        "pages/checklist_records_dashboard/index.html",
        leaf_appearences_chart_data=leaf_appearences_chart_data,
        leaf_colors_chart_data=leaf_colors_chart_data,
        plants=plants,
        charts_filtered_data = plant_growth_data
    )
