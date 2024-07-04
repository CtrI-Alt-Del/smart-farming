from dataclasses import dataclass

from ..base_error import BaseError


@dataclass
class ChecklistRecordNotFoundError(BaseError):
    ui_message: str = "Registro check-list não encontrado"
    internal_message: str = "Checklist record not found"
    status_code: int = 404
