from flask_wtf import FlaskForm

from .fields import EmailField


class RequestPasswordResetForm(FlaskForm, EmailField): ...
