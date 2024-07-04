from dataclasses import dataclass

from ..base_error import BaseError


@dataclass
class HourNotValidError(BaseError):
    ui_message = "Hora não é válido"
    internal_message = "Hour is not valid"
    status_code = 400
