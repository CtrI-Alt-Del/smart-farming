from dataclasses import dataclass

from ..base_error import BaseError


@dataclass
class CookieExpiredError(BaseError):
    ui_message = "Seu token Expirou!, reenvie novamente para o email!"
    internal_message = "Client token has expired"
    status_code = 401
