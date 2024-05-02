from flask import request, render_template

from core.use_cases.plants_records import delete_plants

from core.commons import Error



def delete_plants_view():
    plant_ids = request.form.getlist("plants-ids[]")

    try:
        delete_plants.execute(plant_ids)

        return render_template(
            "pages/plants/index.html",
        )
    except Error as error:
        return "ERROR", error.status_code
