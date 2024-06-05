from flask import render_template

from infra.authentication import auth


@auth.login_middleware
def request_password_reset_page_view():
    return render_template("pages/login/reset_password_page.html")
