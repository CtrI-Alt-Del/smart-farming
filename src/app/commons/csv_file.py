from typing import Dict, List
from werkzeug.datastructures import FileStorage

from providers.data_analyser_provider import DataAnalyserProvider


class CsvFile:
    def __init__(self, csv_file: FileStorage) -> None:
        self.csv_file = csv_file

    def get_records(self) -> List[Dict]:
        data_analyser_provider = DataAnalyserProvider()
        data_analyser_provider.analyse(self.csv_file)

        extension = self.get_extension()

        if extension == "csv":
            data_analyser_provider.read_csv()
        else:
            data_analyser_provider.read_excel()

        records = data_analyser_provider.convert_to_list_of_records()

        return records

    def get_extension(self) -> str:
        return self.csv_file.filename.split(".")[1]
