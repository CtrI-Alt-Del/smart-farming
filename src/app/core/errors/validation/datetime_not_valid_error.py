from dataclasses import dataclass

from ..base_error import BaseError


@dataclass
class DatetimeNotValidError(BaseError):
    ui_message = "Valor de data ou hora mal formatado"
    internal_message = "Datetime value is not valid"
    status_code = 400
