from flask import request, render_template

from core.use_cases.plants import update_active_plant
from core.commons import Error

from infra.authentication import auth


@auth.login_middleware
def update_active_plant_view():
    try:
        user = auth.get_user()
        plant_id = request.form.get("plant")

        update_active_plant.execute(user.id, plant_id)

        return render_template(
            "components/toast_message.html",
            id="active-plant-message",
            success_message="Planta ativa redefinida com sucesso",
        )
    except Error as error:
        return (
            render_template(
                "components/toast_message.html",
                id="active-plant-message",
                success_message="Planta ativa redefinida com sucesso",
                error_message=error.ui_message,
            ),
            error.status_code,
        )
