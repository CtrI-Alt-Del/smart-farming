from dataclasses import dataclass

from ..base_error import BaseError


@dataclass
class TokenNotValidError(BaseError):
    ui_message = "Seu token Expirou!, reenvie novamente para o email!"
    internal_message = "Token for authentication is invalid"
    status_code = 401
