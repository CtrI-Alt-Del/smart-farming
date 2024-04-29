from typing import Dict, List
from werkzeug.datastructures import FileStorage
from math import isnan


from core.commons import Error

from infra.providers.data_analyser_provider import DataAnalyserProvider


class CsvFile:
    def __init__(self, csv_file: FileStorage) -> None:
        self.csv_file = csv_file
        self.data_analyser_provider = DataAnalyserProvider()

    def read(self):
        self.data_analyser_provider.analyse(self.csv_file)

        extension = self.get_extension()

        if extension == "csv" or extension == "txt":
            self.data_analyser_provider.read_csv()
        elif extension == "xlsx":
            self.data_analyser_provider.read_excel()
        else:
            raise Error("Arquivo CSV inválido")

    def get_records(self) -> List[Dict]:
        records = self.data_analyser_provider.convert_to_list_of_records()

        list = []
        for record in records:
            current_record = {}
            for key, value in record.items():
                key = key.lower()
                value = None if isinstance(value, float) and isnan(value) else value
                current_record = {**current_record, key: value}

            print(current_record)
            list.append(current_record)

        return list

    def remove_missing_values(self):
        self.data_analyser_provider.drop_none_values()

    def validate_columns(self, columns: List[str]) -> bool:
        csv_columns = self.data_analyser_provider.get_columns()

        has_valid_columns = set(map(lambda x: x.lower(), csv_columns)) == set(
            map(lambda x: x.lower(), columns)
        )

        if not has_valid_columns:
            raise Error("As colunas do arquivo CSV não estão corretas")

    def get_extension(self) -> str:
        return self.csv_file.filename.split(".")[1]
