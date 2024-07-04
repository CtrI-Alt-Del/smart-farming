from dataclasses import dataclass

from ..base_error import BaseError


@dataclass
class DatetimeNotValidError(BaseError):
    ui_message: str = "Valor de data ou hora mal formatado"
    internal_message: str = "Datetime value is not valid"
    status_code: int = 400
