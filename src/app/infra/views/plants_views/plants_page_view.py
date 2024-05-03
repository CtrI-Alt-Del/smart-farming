from flask import render_template

from infra.repositories import plants_repository
from infra.forms import PlantForm


def plants_page_view():
    plants = plants_repository.get_plants()

    create_plant_form = PlantForm()
    update_plant_form = PlantForm()

    return render_template(
        "pages/plants/index.html",
        create_plant_form=create_plant_form,
        update_plant_form=update_plant_form,
        plants=plants,
    )
