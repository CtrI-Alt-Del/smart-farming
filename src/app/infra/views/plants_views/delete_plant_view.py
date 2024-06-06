from flask import render_template

from core.use_cases.plants import delete_plant, get_plants_page_data

from core.commons import Error

from infra.authentication import auth

@auth.login_middleware
def delete_plant_view(id: str):
    try:
        auth_user = auth.get_user()
        delete_plant.execute(id)

        plants = get_plants_page_data.execute()

        return render_template(
            "pages/plants/plants_cards/index.html",
            plants=plants,
            message="Planta deletada com sucesso",
            action="delete",
            auth_user=auth_user
        )
    except Error as error:
        print(error.ui_message)
        return "ERROR", error.status_code
