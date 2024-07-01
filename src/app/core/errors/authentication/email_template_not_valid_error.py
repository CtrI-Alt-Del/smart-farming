from dataclasses import dataclass

from ..base_error import BaseError


@dataclass
class EmailTemplateNotValidError(BaseError):
    ui_message = "Template de e-mail não fornecido"
    internal_message = "Email template is not provided"
    status_code = 500
