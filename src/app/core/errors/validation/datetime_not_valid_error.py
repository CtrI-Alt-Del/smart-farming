from dataclasses import dataclass

from ..base_error import BaseError


@dataclass
class DatetimeValueNotValidError(BaseError):
    ui_message = "Valor de data não válido"
    internal_message = "Datetime value is not valid"
    status_code = 400
