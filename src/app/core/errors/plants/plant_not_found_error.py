from dataclasses import dataclass

from ..base_error import BaseError


@dataclass
class PlantNotFoundError(BaseError):
    ui_message = "Planta não encontrado"
    internal_message = "Plant is not found"
    status_code = 404
