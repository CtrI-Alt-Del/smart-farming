from dataclasses import dataclass

from ..base_error import BaseError


@dataclass
class DateNotValidError(BaseError):
    ui_message = "Valor de data não válido"
    internal_message = "Date value is not valid"
    status_code = 400
