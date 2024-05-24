from flask import render_template


def delete_plant_alert_view(id: str):
    return render_template("pages/plants/delete_plant_alert.html", plant_id=id)
