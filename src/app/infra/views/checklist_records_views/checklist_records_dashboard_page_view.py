from json import dumps
from flask import render_template, flash, redirect, url_for

from core.use_cases.checklist_records import get_checklist_dashboard_page_data
from core.constants import LEAF_COLORS
from core.commons import DaysRange, Error

from infra.constants import LEAF_COLORS_CHART_LEGEND_HEX_COLORS
from infra.utils import JSONEncoder


def checklist_records_dashboard_page_view():
    try:
        data = get_checklist_dashboard_page_data.execute()

        if len(data) == 0:
            raise Error("Nenhum registro check-list encontrado", status_code=404)

        leaf_appearences_chart_data = dumps(
            data["days_count_by_leaf_appearance_and_plant"], ensure_ascii=False
        )

        leaf_colors_chart_data = dumps(
            data["days_count_by_leaf_color_and_plant"], ensure_ascii=False
        )

        plant_growth_chart_data = dumps(
            data["plant_growth_chart_data"], cls=JSONEncoder
        )

        plants = data["plants"]

        days_ranges = DaysRange()

        return render_template(
            "pages/checklist_records_dashboard/index.html",
            leaf_appearences_chart_data=leaf_appearences_chart_data,
            leaf_colors_chart_data=leaf_colors_chart_data,
            leaf_colors_chart_hex_colors=LEAF_COLORS_CHART_LEGEND_HEX_COLORS,
            leaf_colors=LEAF_COLORS,
            plant_growth_chart_data=plant_growth_chart_data,
            days_ranges=days_ranges.get_value(),
            plants=plants,
        )
    except Error as error:
        flash(error.ui_message, "error")
        return redirect(
            url_for(
                "plants_views.plants_page_view"
                if "planta" in error.ui_message.lower()
                else "checklist_records_views.checklist_records_table_page_view"
            )
        )
