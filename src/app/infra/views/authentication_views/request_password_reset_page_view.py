from flask import render_template

from core.commons import Error

from infra.forms import RequestPasswordResetForm


def request_password_reset_page_view():
    form = RequestPasswordResetForm()

    try:
        return render_template("pages/request_password_reset/index.html", form=form)
    except Error as error:
        raise error
