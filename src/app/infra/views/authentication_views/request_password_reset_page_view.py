from flask import render_template, make_responseq

from core.use_cases.request_password_reset import request_password_reset

from core.commons import Error

def request_password_reset_page_view():
    
    try:    
        email_template = render_template("components/email.html")
        Request_password_reset = request_password_reset.RequestPasswordReset.execute(
            "ctralaltdelsup@gmail.com", email_template
        )
        # token = token
        print(Request_password_reset, flush=True)

        return render_template(
            "pages/request_password_reset/index.html",
            request_password_reset=Request_password_reset,
        )
    except Error as error:
        raise error
