from dataclasses import dataclass

from ..base_error import BaseError


@dataclass
class CredentialsNotValidError(BaseError):
    ui_message = "E-mail ou senha incorretos"
    internal_message = "E-mail or password invalid"
    status_code = 401
