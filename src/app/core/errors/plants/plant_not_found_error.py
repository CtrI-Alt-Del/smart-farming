from dataclasses import dataclass

from ..base_error import BaseError


@dataclass
class PlantNotFoundError(BaseError):
    ui_message: str = "Planta não encontrada"
    internal_message: str = "Plant is not found"
    status_code: int = 404
