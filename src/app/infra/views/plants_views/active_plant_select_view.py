from flask import render_template

from core.constants import ADMIN_USER_EMAIL
from infra.repositories import plants_repository, users_repository

from infra.authentication import auth


def active_plant_select_view():
    if not auth.get_user():
        return " "

    try:
        plants = plants_repository.get_plants()
        active_plant_id = users_repository.get_user_active_plant_id(
            email=ADMIN_USER_EMAIL
        )

        return render_template(
            "pages/plants/active_plant_select.html",
            plants=plants,
            active_plant_id=active_plant_id,
        )
    except Exception:
        return " "
