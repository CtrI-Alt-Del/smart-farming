from dataclasses import dataclass

from ..base_error import BaseError


@dataclass
class NewPasswordNotValidError(BaseError):
    ui_message = "Nova senha não é válida"
    internal_message = "New password is not valid"
    status_code = 400
