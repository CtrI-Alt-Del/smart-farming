from typing import Dict, List
from werkzeug.datastructures import FileStorage

from core.interfaces.providers import DataAnalyserProviderInterface
from core.errors.validation import CSVFileNotValidError, CSVColumnsNotValidError


class CsvFile:
    def __init__(
        self,
        file: FileStorage,
        data_analyser_provider: DataAnalyserProviderInterface,
    ):
        if not isinstance(file, FileStorage):
            raise CSVFileNotValidError()

        self._file = file
        self._data_analyser_provider = data_analyser_provider

    def read(self):
        extension = self.__get_extension()

        if extension in ["csv", "txt"]:
            self._data_analyser_provider.read_csv(self._file)
        elif extension == "xlsx":
            self._data_analyser_provider.read_excel(self._file)
        else:
            raise CSVFileNotValidError()

    def get_records(self) -> List[Dict]:
        records = self._data_analyser_provider.convert_to_list_of_records()

        records_list = []
        for record in records:
            records_list.append({key.lower(): value for key, value in record.items()})

        return records_list

    def validate_columns(self, columns: List[str]):
        csv_columns = self._data_analyser_provider.get_columns()

        has_valid_columns = set(map(lambda x: x.lower(), csv_columns)) == set(
            map(lambda x: x.lower(), columns)
        )

        if not has_valid_columns:
            raise CSVColumnsNotValidError()

    def __get_extension(self) -> str:
        return self._file.filename.split(".")[1]
