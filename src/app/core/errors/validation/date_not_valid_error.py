from dataclasses import dataclass

from ..base_error import BaseError


@dataclass
class DateNotValidError(BaseError):
    ui_message: str = "Valor de data não válido"
    internal_message: str = "Date value is not valid"
    status_code: int = 400
