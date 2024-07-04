from dataclasses import dataclass

from ..base_error import BaseError


@dataclass
class UserEmailNotValidError(BaseError):
    ui_message = "E-mail de usuário não fornecido"
    internal_message = "User email is not provided"
    status_code = 500
