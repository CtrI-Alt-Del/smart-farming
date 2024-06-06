from flask import request, render_template

from core.use_cases.plants import create_plant_by_form, get_plants_page_data
from core.commons import Error

from infra.forms import PlantForm

from infra.authentication import auth


@auth.login_middleware
def create_plant_view():

    plant_form = PlantForm(request.form)

    try:
        
        auth_user = auth.get_user()

        if not plant_form.validate_on_submit():
            raise Error("Formulário inválido")

        create_plant_by_form.execute(
            {"name": plant_form.name.data, "hex_color": plant_form.hex_color.data}
        )

        plants = get_plants_page_data.execute()

        return render_template(
            "pages/plants/plants_cards/index.html",
            plants=plants,
            action="create",
            auth_user=auth_user
        )
    except Error as error:
        return (
            render_template(
                "pages/plants/create_plant_form/fields.html",
                plant_form=plant_form,
                create_plant_form=plant_form,
            ),
            error.status_code,
        )
