from dataclasses import dataclass

from ..base_error import BaseError


@dataclass
class UserNotFoundError(BaseError):
    ui_message = "Usuário não encontrado"
    internal_message = "User not found"
    status_code = 404
