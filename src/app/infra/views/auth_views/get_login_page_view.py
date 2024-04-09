from flask import render_template


def get_login_page_view():
    return render_template("pages/login/index.html")
