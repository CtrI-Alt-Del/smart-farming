from typing import Dict

from common.csv_file import CsvFile


class CreateSensorsByCsvFile:
    def execute(self, data: Dict):
        csv_file = CsvFile(data)
        csv_file.validate()
