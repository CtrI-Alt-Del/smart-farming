from os import getenv
from uuid import uuid4

from flask import render_template, make_response, request

from core.use_cases.authentication import request_password_reset

from core.commons import Error

from infra.authentication import auth
from infra.constants import COOKIES
from infra.forms import RequestPasswordResetForm

URL = getenv("URL")


def request_password_reset_view():
    form = RequestPasswordResetForm(request.form)

    try:
        if not form.validate_on_submit():
            raise Error(ui_message="Formulário inválido", status_code=400)

        password_reset_token = uuid4()
        token = auth.generate_hash(str(password_reset_token))

        user_email = request.form.get("email")

        email_template = render_template(
            "components/password_reset_email.html", url=URL, token=token
        )

        response = make_response(
            render_template(
                "pages/request_password_reset/email_field.html",
                form=form,
                success_message="Enviamos um e-mail para você redefinir a senha",
            )
        )

        response.set_cookie(
            COOKIES["keys"]["password_reset_token"],
            str(password_reset_token),
            max_age=900,  # 15 minutes
        )

        request_password_reset.execute(user_email, email_template)

        return response
    except Error as error:
        return (
            render_template(
                "pages/request_password_reset/email_field.html",
                form=form,
                error_message=error.ui_message,
            ),
            error.status_code,
        )
