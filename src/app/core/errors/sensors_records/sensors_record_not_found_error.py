from dataclasses import dataclass

from ..base_error import BaseError


@dataclass
class SensorsRecordNotFoundError(BaseError):
    ui_message: str = "Registro dos sensores não encontrado"
    internal_message: str = "Sensors record not found"
    status_code: int = 404
