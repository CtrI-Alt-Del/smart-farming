from typing import Dict, List

from werkzeug.datastructures import FileStorage

from pandas import DataFrame, read_excel, read_csv


class DataAnalyserProvider:
    data: DataFrame | None

    def __init__(self) -> None:
        self.data = None

    def analyse(self, data) -> None:
        self.data = DataFrame(data)

    def read_excel(self, file: FileStorage) -> None:
        self.data = read_excel(file)

    def read_csv(self, file: FileStorage) -> None:
        self.data = read_csv(file)

    def convert_to_excel(self, folder: str, filename: str) -> None:
        if self.__has_dataframe():
            self.data.to_excel(f"{folder}/{filename}", index=False)

    def convert_to_list_of_records(self) -> List[Dict] | None:
        if self.__has_dataframe():
            return self.data.to_dict("records")

        return None

    def get_data(self):
        return self.data

    def __has_dataframe(self) -> bool:
        return self.data is not None
