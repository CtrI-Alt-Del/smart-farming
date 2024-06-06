from flask import render_template



def reset_password_view():
    return render_template("pages/reset_password/index.html")