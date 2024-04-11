from flask import render_template


def plants_page_view():
    return render_template("pages/plants/index.html")
