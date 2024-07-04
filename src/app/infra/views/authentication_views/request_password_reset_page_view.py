from flask import render_template

from infra.forms import RequestPasswordResetForm


def request_password_reset_page_view():
    form = RequestPasswordResetForm()

    return render_template("pages/request_password_reset/index.html", form=form)
