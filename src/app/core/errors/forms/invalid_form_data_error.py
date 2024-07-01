from dataclasses import dataclass

from ..base_error import BaseError


@dataclass
class InvalidFormDataError(BaseError):
    ui_message = "Formulário inválido"
    internal_message = "Invalid form data"
    status_code = 400
