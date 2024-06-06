from flask import request, render_template

from core.use_cases.plants import filter_plants

from core.commons import Error

from infra.authentication import auth


@auth.login_middleware
def filter_plants_view():
    plant_name = request.args.get("search", "")

    try:
        auth_user = auth.get_user()
        plants = filter_plants.execute(plant_name)

        return render_template("pages/plants/plants_cards/index.html", plants=plants,auth_user=auth_user)
    except Error as error:
        print(error)
        return "ERROR", error.status_code
