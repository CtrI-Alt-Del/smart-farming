from flask import render_template, flash, request, make_response, redirect


from core.errors.authentication import CookieExpiredError, TokenNotValidError

from infra.authentication import auth
from infra.constants import COOKIES
from infra.forms import ResetPasswordForm


def reset_password_page_view():
    try:
        email_token = request.args.get("token")
        cookie = request.cookies.get(COOKIES["keys"]["password_reset_token"])
        form = ResetPasswordForm()

        if not cookie:
            raise CookieExpiredError()

        is_token_valid = auth.check_hash(email_token, cookie)

        if is_token_valid:
            page_template = render_template(
                "pages/reset_password/index.html", form=form
            )
            response = make_response(page_template)

            return response
        else:
            raise TokenNotValidError()

    except Exception as error:
        flash(error.ui_message, "error")

        return redirect("/login")
