from flask import render_template

from infra.authentication import auth


@auth.login_middleware
def delete_plant_alert_view(id: str):
    return render_template("pages/plants/delete_plant_alert.html", plant_id=id)
