from dataclasses import dataclass

from ..base_error import BaseError


@dataclass
class CSVColumnsNotValidError(BaseError):
    ui_message = "As colunas do arquivo CSV não estão corretas"
    internal_message = "CSV file columns are not valid"
    status_code = 400
