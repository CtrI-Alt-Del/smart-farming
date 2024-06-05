from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, ValidationError

import re


class LoginForm(FlaskForm):
    email = EmailField(
        "E-mail",
        validators=[DataRequired(), Email()],
    )

    password = PasswordField(
        "Senha",
        validators=[DataRequired()],
    )

    remember_me = BooleanField("Lembre-se de mim")

    def validate_password(self, password):
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[\W_]).{6,}$"

        if not re.match(pattern, password.data):
            raise ValidationError(
                "Senha inválida. Deve conter pelo menos 6 caracteres, uma letra minúscula, uma letra maiúscula e um caractere especial."
            )
