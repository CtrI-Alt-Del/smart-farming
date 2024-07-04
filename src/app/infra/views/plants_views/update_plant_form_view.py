from flask import render_template

from infra.factories.use_cases.plants import get_plant_by_id
from core.commons import Error

from infra.forms import PlantForm
from infra.authentication import auth


@auth.login_middleware
def update_plant_form_view(id: str):
    try:
        plant = get_plant_by_id.execute(id)
        plant_form = PlantForm(plant=plant)

        return render_template(
            "pages/plants/update_plant_form/index.html",
            update_plant_form=plant_form,
            plant_id=plant.id,
        )
    except Error as error:
        return "ERROR", error.status_code
