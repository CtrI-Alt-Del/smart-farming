from flask import render_template

from core.commons import Error


def request_password_reset_page_view():

    try:
        return render_template(
            "pages/request_password_reset/index.html",
        )
    except Error as error:
        raise error
