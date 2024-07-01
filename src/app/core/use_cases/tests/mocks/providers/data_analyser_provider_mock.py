from werkzeug.datastructures import FileStorage

from core.interfaces.providers import DataAnalyserProviderInterface


class DataAnalyserProviderMock(DataAnalyserProviderInterface):
    _data = None

    def analyse(self, data): ...

    def read_excel(self, file: FileStorage):
        self._data = "excel file data"

    def read_csv(self, file: FileStorage):
        self._data = "csv text file data"

    def get_columns(self): ...

    def convert_to_excel(self, folder: str, filename: str): ...

    def convert_to_list_of_records(self): ...

    def get_data(self):
        return self._data
