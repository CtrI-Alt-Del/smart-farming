from flask import request, render_template

from core.use_cases.plants import update_plant
from core.commons import Error

from infra.forms import PlantForm

from infra.authentication import auth

@auth.login_middleware
def update_plant_view(id: str):
    plant_form = PlantForm(formdata=request.form)

    try:
        auth_user = auth.get_user()
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
            update_message="Planta atualizada com sucesso",
            auth_user=auth_user
        )
    except Error as error:
        print(plant_form.hex_color.default, flush=True)
        return (
            render_template(
                "pages/plants/update_plant_form/fields.html",
                update_plant_form=plant_form,
                auth_user=auth_user
            ),
            error.status_code,
        )
