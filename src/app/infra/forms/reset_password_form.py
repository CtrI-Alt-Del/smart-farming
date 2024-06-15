from flask_wtf import FlaskForm

from .fields import PasswordField_, ConfirmPasswordField


class ResetPasswordForm(FlaskForm, PasswordField_, ConfirmPasswordField): ...
