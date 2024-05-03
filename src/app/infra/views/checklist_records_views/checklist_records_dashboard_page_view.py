from json import dumps
from flask import render_template

from core.use_cases.checklist_records import get_checklist_dashboard_page_data
from core.constants import LEAF_COLORS

from infra.constants import LEAF_COLORS_CHART_LEGEND_HEX_COLORS
from infra.utils import JSONEncoder


def checklist_records_dashboard_page_view():
    data = get_checklist_dashboard_page_data.execute()

    leaf_appearences_chart_data = dumps(
        data["days_count_by_leaf_appearance_and_plant"], ensure_ascii=False
    )

    leaf_colors_chart_data = dumps(
        data["days_count_by_leaf_color_and_plant"], ensure_ascii=False
    )

    plant_growth_chart_data = dumps(data["plant_growth_chart_data"], cls=JSONEncoder)

    plants = data["plants"]

    # print(dumps(data["plant_growth_chart_data"]), flush=True)

    return render_template(
        "pages/checklist_records_dashboard/index.html",
        leaf_appearences_chart_data=leaf_appearences_chart_data,
        leaf_colors_chart_data=leaf_colors_chart_data,
        leaf_colors_chart_hex_colors=LEAF_COLORS_CHART_LEGEND_HEX_COLORS,
        leaf_colors=LEAF_COLORS,
        plant_growth_chart_data=plant_growth_chart_data,
        plants=plants,
    )
