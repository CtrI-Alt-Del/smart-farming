from flask import request, render_template

from core.use_cases.plants_records import update_plants
from core.commons import Error

from infra.forms import PlantForm


def update_plant_view(id: str):
    plant_form = PlantForm(formdata=request.form)

    try:
        if not plant_form.validate_on_submit():
            raise Error("Formulário inválido")

        updated_plant = update_plants.execute(
            {
                "name": plant_form.plant_name.data,
                "hex_color": plant_form.hex_color.data,
                "checklist_record_id": id,
            },
        )

        return render_template(
            "pages/plants/index.html",
            plant=updated_plant,
        )
    except Error as error:
        print(plant_form.errors, flush=True)
        return "ERROR", error.status_code
