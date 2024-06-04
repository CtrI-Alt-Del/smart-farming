from flask import render_template


def reset_password_view():
    print("banana")
    return render_template("pages/login/reset_password_page.html")