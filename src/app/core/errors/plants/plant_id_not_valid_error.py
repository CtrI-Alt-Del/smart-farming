from dataclasses import dataclass

from ..base_error import BaseError


@dataclass
class PlantIdNotValidError(BaseError):
    ui_message = "Planta inválida"
    internal_message = "Plant id is not valid"
    status_code = 400
