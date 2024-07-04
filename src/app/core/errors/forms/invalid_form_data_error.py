from dataclasses import dataclass

from ..base_error import BaseError


@dataclass
class InvalidFormDataError(BaseError):
    ui_message: str = "Formulário inválido"
    internal_message: str = "Invalid form data"
    status_code: int = 400
