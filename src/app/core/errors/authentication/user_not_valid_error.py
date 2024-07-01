from dataclasses import dataclass

from ..base_error import BaseError


@dataclass
class UserNotValidError(BaseError):
    ui_message = "Usuário não fornecido"
    internal_message = "User not provided"
    status_code = 500
