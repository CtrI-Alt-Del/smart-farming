from flask import render_template

def error_page_view():
    return render_template("pages/internal_server_error/index.html")

