from typing import Dict, List
from werkzeug.datastructures import FileStorage

from core.commons import Error

from infra.providers.data_analyser_provider import DataAnalyserProvider


class CsvFile:
    def __init__(self, csv_file: FileStorage) -> None:
        self.csv_file = csv_file
        self.data_analyser_provider = DataAnalyserProvider()

    def read(self):
        extension = self.get_extension()

        if extension in ["csv", "txt"]:
            self.data_analyser_provider.read_csv(self.csv_file)
        elif extension == "xlsx":
            self.data_analyser_provider.read_excel(self.csv_file)
        else:
            raise Error("Arquivo CSV inválido")

    def get_records(self) -> List[Dict]:
        records = self.data_analyser_provider.convert_to_list_of_records()

        records_list = []
        for record in records:
            records_list.append({key.lower(): value for key, value in record.items()})

        return records_list

    def validate_columns(self, columns: List[str]) -> bool:
        csv_columns = self.data_analyser_provider.get_columns()

        has_valid_columns = set(map(lambda x: x.lower(), csv_columns)) == set(
            map(lambda x: x.lower(), columns)
        )

        if not has_valid_columns:
            raise Error("As colunas do arquivo CSV não estão corretas")

    def get_extension(self) -> str:
        return self.csv_file.filename.split(".")[1]
