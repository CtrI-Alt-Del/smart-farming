from flask import Flask
from flask_login import (
    LoginManager,
)
from flask_bcrypt import Bcrypt

from .password import Password
from .load_user import load_user

bcrypt = Bcrypt()

password = Password(bcrypt)


def init_auth(app: Flask):
    login_manager = LoginManager()

    login_manager.init_app(app)
    login_manager.user_loader(load_user)
    login_manager.login_view = "auth_views.login_view"
    login_manager.login_message = "Por favor, faça seu login antes"
    login_manager.login_message_category = "error"

    bcrypt.init_app(app)
