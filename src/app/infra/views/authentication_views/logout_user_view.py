from flask import url_for, redirect

from infra.authentication import auth


def logout_user_view():
    try:
        auth.logout()

        url = url_for("authentication_views.login_page_view")

        return redirect(url)

    except Exception:
        return "Error ao tentar fazer logout", 500
