from json import dumps

from flask import redirect, url_for, flash, make_response, request

from core.use_cases.plants_records import create_plants_by_form
from core.commons import Error

from infra.forms import PlantForm


def create_plant_by_form_view():
    plant_form = PlantForm(request.form)

    response = make_response(
        redirect(url_for(""))
    )

    if plant_form.validate_on_submit():
        try:
            create_plants_by_form.CreatePlantByForm.execute(
                {
                    "name": plant_form.plant_name.data,
                    "hex_color": plant_form.hex_color.data
                }
            )

            flash("Registro plant salvo com sucesso", "success")
            return response
        except Error as error:
            flash(error.ui_message, "error")
            return response

    response.set_cookie(
        "plant_form_errors", dumps(plant_form.errors)
    )

    flash("Registro plant inválido", "error")
    return response
