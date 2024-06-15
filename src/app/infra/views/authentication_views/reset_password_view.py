from flask import render_template, request, make_response, redirect


from core.commons import Error

from infra.authentication import auth


def reset_password_view():
    try:
        email_token = request.args.get("token")
        cookie = request.cookies.get("Petros")
        if not cookie:
            raise Error(
                internal_message="Client token has expired",
                ui_message="Seu token Expirou!,reenvie novamente para o email!",
                status_code=401,
            )
        if auth.check_hash(email_token, cookie):
            response = make_response(render_template("pages/reset_password/index.html"))
            return response
        else:
            return redirect("/login")
    except Error:
        raise Error(
            internal_message="Client token has expired",
            ui_message="Seu token Expirou!",
            status_code=401,
        )
