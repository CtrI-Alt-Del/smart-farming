from flask import render_template, make_response, request

from core.use_cases.authentication import request_password_reset

from core.commons import Error

from infra.authentication import auth
import uuid



def request_password_reset_send_view():
    try:
        password_reset_token = uuid.uuid4()
        uuid_bytes = password_reset_token.bytes
        token = auth.generate_hash(uuid_bytes)

        user_email = request.form.get("email")

        email_template = render_template("components/email.html", token=token)

        response = make_response(render_template("components/email_sucess.html"))

        response.set_cookie("Petros", token, max_age=900, secure=True, httponly=True)

        request_password_reset.execute(user_email, email_template)

        return response
    except Error as error:
        raise error
