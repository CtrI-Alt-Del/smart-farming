from dataclasses import dataclass

from ..base_error import BaseError


@dataclass
class PlantNameNotValidError(BaseError):
    ui_message = "Nome de planta inválido"
    internal_message = "Plant name is not valid"
    status_code = 400
