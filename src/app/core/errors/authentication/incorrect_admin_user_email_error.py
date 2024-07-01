from dataclasses import dataclass

from ..base_error import BaseError


@dataclass
class IncorrectAdminUserEmailError(BaseError):
    ui_message = "E-mail fornecido não é o e-mail do administrador"
    internal_message = "User email is not equal to admin user email"
    status_code = 500
