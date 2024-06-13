from flask import render_template,request



def reset_password_view():
    print(request.cookies.get("Petros"), flush=True)

    return render_template("pages/reset_password/index.html")