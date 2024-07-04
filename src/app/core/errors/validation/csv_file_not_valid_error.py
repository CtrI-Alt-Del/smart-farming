from dataclasses import dataclass

from ..base_error import BaseError


@dataclass
class CSVFileNotValidError(BaseError):
    ui_message = "Arquivo CSV inválido"
    internal_message = "CSV file is not valid"
    status_code = 400
