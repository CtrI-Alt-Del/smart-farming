from dataclasses import dataclass

from ..base_error import BaseError


@dataclass
class PlantNameAlreadyInUseError(BaseError):
    ui_message = "Nome de planta já utilizada"
    internal_message = "Plant name already in use"
    status_code = 409
