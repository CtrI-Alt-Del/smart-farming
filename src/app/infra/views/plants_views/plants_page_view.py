from flask import request, render_template

from core.use_cases.plants import filter_plants

from infra.forms import PlantForm


def plants_page_view():
    plant_name = request.args.get("search", "")

    plants = filter_plants.execute(plant_name)

    create_plant_form = PlantForm()
    update_plant_form = PlantForm()

    return render_template(
        "pages/plants/index.html",
        create_plant_form=create_plant_form,
        update_plant_form=update_plant_form,
        plants=plants,
    )
