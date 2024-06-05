from flask import request, render_template

from infra.forms import LoginForm


def login_page_view():
    login_form = LoginForm()

    next_page_param = request.args.get("next")

    return render_template(
        "pages/login/index.html", login_form=login_form, next_page_param=next_page_param
    )
