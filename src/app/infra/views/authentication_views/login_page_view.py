from flask import render_template

from infra.forms import LoginForm


def login_page_view():
    login_form = LoginForm()

    return render_template("pages/login/index.html", login_form=login_form)
