from flask import request, render_template

from core.use_cases.plants_records import create_plant_by_form, get_plants_page_data
from core.commons import Error

from infra.forms import PlantForm


def create_plant_by_form_view():
    plant_form = PlantForm(request.form)

    try:
        if not plant_form.validate_on_submit():
            raise Error("Formulário inválido")

        create_plant_by_form.execute(
            {"name": plant_form.name.data, "hex_color": plant_form.hex_color.data}
        )

        plants = get_plants_page_data.execute()

        return render_template("")
    except Error as error:
        print(error.ui_message, flush=True)
        return "ERROR", error.status_code

