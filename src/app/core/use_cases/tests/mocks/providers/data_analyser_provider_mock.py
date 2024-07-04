from werkzeug.datastructures import FileStorage

from core.interfaces.providers import DataAnalyserProviderInterface


class DataAnalyserProviderMock(DataAnalyserProviderInterface):
    _data = None
    _csv_file = None

    def analyse(self, data):
        self._data = data

    def read_excel(self, file: FileStorage):
        self._data = "excel file data"

    def read_csv(self, file: FileStorage):
        self._data = "csv text file data"

    def get_columns(self): ...

    def convert_to_excel(self, folder: str, filename: str):
        self._csv_file = {"path": f"{folder}/{filename}", "data": self._data}

    def convert_to_list_of_records(self): ...

    def get_data(self):
        return self._data

    @property
    def csv_file(self):
        return self._csv_file
