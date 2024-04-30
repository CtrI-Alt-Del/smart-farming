from flask import request

from core.use_cases.plants_records import create_plant_by_form, get_plants_page_data

from core.commons import Error

from infra.forms import PlantForm


def create_plant_by_form_view():
    plant_form = PlantForm(request.form)

    plants = []

    try:
        if not plant_form.validate_on_submit():
            raise Error("Formulário inválido")

        create_plant_by_form.execute(
            {"name": plant_form.plant_name.data, "hex_color": plant_form.hex_color.data}
        )

        plants = get_plants_page_data.execute()

    except Error as error:
        return "ERROR", error.status_code

    return str(plants)
