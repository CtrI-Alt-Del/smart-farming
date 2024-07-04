from flask import request, render_template

from infra.factories.use_cases.plants import filter_plants

from infra.forms import PlantForm
from infra.authentication import auth
from infra.repositories import plants_repository


def plants_page_view():

    auth_user = auth.get_user()

    plant_name = request.args.get("search", "")

    all_plants = plants_repository.get_plants()

    plants = filter_plants.execute(plant_name)

    create_plant_form = PlantForm()
    update_plant_form = PlantForm()

    return render_template(
        "pages/plants/index.html",
        create_plant_form=create_plant_form,
        update_plant_form=update_plant_form,
        plants=plants,
        all_plants=all_plants,
        auth_user=auth_user,
    )
