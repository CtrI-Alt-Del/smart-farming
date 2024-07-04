from flask import request, render_template, url_for, make_response

from core.errors.forms import InvalidFormDataError

from infra.factories.use_cases.authentication import login_user
from infra.forms import LoginForm


def login_user_view():
    login_form = LoginForm(request.form)

    try:
        if not login_form.validate_on_submit():
            raise InvalidFormDataError()

        response = make_response()

        next_page_param = request.args.get("next", None)

        url = url_for("sensors_records_views.last_sensors_record_page_view")

        if isinstance(next_page_param, str) and next_page_param[0] == "/":
            url = next_page_param

        response.headers["hx-redirect"] = url

        email = login_form.email.data
        password = login_form.password.data
        remember_me = login_form.remember_me.data

        login_user.execute(
            email=email, password=password, should_remember_user=remember_me
        )
        return response

    except Exception as error:
        return (
            render_template(
                "pages/login/login_form.html",
                login_form=login_form,
                error_message=error,
            ),
            error.status_code,
        )
