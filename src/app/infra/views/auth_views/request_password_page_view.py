from flask import render_template


def get_request_password_page_view():
    return render_template("pages/reuqest_password_reset.html")
