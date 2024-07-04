from dataclasses import dataclass

from ..base_error import BaseError


@dataclass
class ChecklistRecordNotValidError(BaseError):
    ui_message = "Registro check-list não válido"
    internal_message = "Checklist Record is not valid"
    status_code = 400
