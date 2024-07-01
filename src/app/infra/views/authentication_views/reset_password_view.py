from flask import render_template, request, make_response


from core.use_cases.authentication import reset_password
from core.errors.forms import InvalidFormDataError

from infra.forms import ResetPasswordForm
from infra.constants import COOKIES


def reset_password_view():
    form = ResetPasswordForm(request.form)

    try:
        if not form.validate_on_submit():
            raise InvalidFormDataError()

        new_password = form.password.data

        reset_password.execute(new_password)

        respose = make_response(
            render_template("pages/reset_password/success_message.html")
        )
        respose.delete_cookie(COOKIES["keys"]["password_reset_token"])
        return respose

    except Exception as error:
        return (
            render_template("pages/reset_password/fields.html", form=form),
            error.status_code,
        )
