from flask_wtf import FlaskForm
from wtforms import BooleanField

from .fields import EmailField, PasswordField_


class LoginForm(FlaskForm, EmailField, PasswordField_):
    remember_me = BooleanField("Lembre-se de mim")
