from flask import render_template

from core.commons import Error
from infra.repositories import plants_repository

from infra.forms import PlantForm


def plant_table_page_view():
    plants = plants_repository.get_plants()

    create_plant_record_form = PlantForm()
    update_plant_record_form = PlantForm()

    try:
        plants

        return render_template(
            "pages/plants/index.html",
            create_plant_form=create_plant_record_form,
            update_plant_form=update_plant_record_form,
            plants=plants,
        )
    except Error:
        return "500 ERROR PAGE"
