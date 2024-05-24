from flask import render_template

from core.use_cases.plants import delete_plant, get_plants_page_data

from core.commons import Error


def delete_plant_view(id: str):
    try:
        delete_plant.execute(id)

        plants = get_plants_page_data.execute()

        return render_template(
            "pages/plants/plants_cards/index.html",
            plants=plants,
            message="Planta deletada com sucesso",
            action="delete",
        )
    except Error as error:
        print(error.ui_message)
        return "ERROR", error.status_code
