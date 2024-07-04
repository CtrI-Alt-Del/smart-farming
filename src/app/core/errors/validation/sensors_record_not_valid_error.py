from dataclasses import dataclass

from ..base_error import BaseError


@dataclass
class SensorsRecordNotValidError(BaseError):
    ui_message = "Registro dos sensores não válido"
    internal_message = "Sensors Record is not valid"
    status_code = 400
