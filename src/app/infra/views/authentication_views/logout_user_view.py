from flask import url_for, redirect

from core.errors.authentication import LogoutFailedError
from infra.authentication import auth


def logout_user_view():
    try:
        has_logout = auth.logout()

        if not has_logout:
            raise LogoutFailedError()

        url = url_for("authentication_views.login_page_view")

        return redirect(url)

    except Exception as error:
        return error.ui_message, error.status_code
