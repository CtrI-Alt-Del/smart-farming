from flask import request, render_template

from core.use_cases.plants_records import get_plant_by_id
from core.commons import Error

from infra.forms import PlantForm


def update_plant_form_view(id: str):
    try:
        plant = get_plant_by_id.execute()

        return render_template(
            "pages/plants/create_plant_form/index.html",
            plant=plant,
        )
    except Error as error:
        print(plant_form.errors, flush=True)
        return "ERROR", error.status_code
