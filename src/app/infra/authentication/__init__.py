from flask import Flask
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

from .auth import Auth

bcrypt = Bcrypt()

auth = Auth(bcrypt)


def init_authentication(app: Flask):
    login_manager = LoginManager()

    login_manager.init_app(app)
    login_manager.user_loader(auth.load_user)
    login_manager.login_view = "authentication_views.login_page_view"
    login_manager.login_message = "Por favor, faça seu login antes"
    login_manager.login_message_category = "error"

    bcrypt.init_app(app)
