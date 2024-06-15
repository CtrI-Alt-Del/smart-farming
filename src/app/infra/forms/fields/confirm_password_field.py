from wtforms import PasswordField
from wtforms.validators import EqualTo


class ConfirmPasswordField:
    confirm_password = PasswordField(
        "Confirme sua senha",
        validators=[EqualTo("password", message="As senhas devem ser iguais")],
    )
