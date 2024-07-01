from dataclasses import dataclass

from ..base_error import BaseError


@dataclass
class SenderPasswordNotProvidedError(BaseError):
    ui_message = "Senha necessária para enviar o email não fornecida"
    internal_message = "Email sender password is not provided"
    status_code = 500
