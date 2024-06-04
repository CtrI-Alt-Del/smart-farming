from flask import render_template


def get_confirmation_page_view():
    return render_template("pages/request_password_reset.html")
