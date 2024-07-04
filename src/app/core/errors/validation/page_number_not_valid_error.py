from dataclasses import dataclass

from ..base_error import BaseError


@dataclass
class PageNumberNotValidError(BaseError):
    ui_message = "Número de página inválido"
    internal_message = "Page number value is not valid"
    status_code = 400
