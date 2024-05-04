from flask import request, render_template

from core.use_cases.plants import update_plant
from core.commons import Error

from infra.forms import PlantForm


def update_plant_view(id: str):
    plant_form = PlantForm(formdata=request.form)

    try:
        if not plant_form.validate_on_submit():
            raise Error("Formulário inválido")

        updated_plant = update_plant.execute(
            {
                "name": plant_form.name.data,
                "hex_color": plant_form.hex_color.data,
            },
            id,
        )

        return render_template(
            "pages/plants/plants_cards/card.html",
            plant=updated_plant,
        )
    except Error as error:
        return "ERROR", error.status_code
