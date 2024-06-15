from flask import render_template, request , make_response


from core.commons import Error

from infra.authentication import auth

from core.use_cases.authentication import reset_password


from infra.authentication.auth_user import AuthUser


def reset_password_send_view():

    try:
        print("esse e o id",AuthUser().get_id(),flush=True)
        
        new_password = request.form.get("password")
        confirm_password = request.form.get("confirmPassword")
        user_id = "bananinha"#user id go here
        if new_password == confirm_password:
            confirm_password = auth.generate_hash(confirm_password)
            reset_password.execute(user_id,confirm_password)
            
            respose = make_response(render_template("components/reset_sucess.html"))
            respose.delete_cookie("Petros")
            return respose
        else:
            raise Error(ui_message="Senhas não são iguais",internal_message="password given were not equal")       
    except Error as error:
        raise error
    
    ##TODO: altough password is changing in db is not allowing me to enter even with the correct password
    ##TODO: get user id by some god forsaken way,as Petros intended
    
    