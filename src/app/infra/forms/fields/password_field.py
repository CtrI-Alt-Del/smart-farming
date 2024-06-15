from re import match

from wtforms import PasswordField as Field
from wtforms.validators import DataRequired, ValidationError


class PasswordField_:
    password = Field(
        "Senha",
        validators=[DataRequired(message="Senha é obrigatória")],
    )

    def validate_password(self, password):
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[\W_]).{6,}$"

        if not match(pattern, password.data):
            raise ValidationError(
                "Senha inválida. Deve conter pelo menos 6 caracteres, uma letra minúscula, uma letra maiúscula e um caractere especial."
            )
