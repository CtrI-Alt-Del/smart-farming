from dataclasses import dataclass

from ..base_error import BaseError


@dataclass
class LogoutFailedError(BaseError):
    ui_message = "Erro interno ao fazer logout"
    internal_message = "Failed to logout"
    status_code = 500
