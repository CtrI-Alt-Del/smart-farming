from typing import List, Dict

from werkzeug.datastructures import FileStorage

from pandas import DataFrame, read_csv, read_excel


class DataAnalyserProvider:
    dataframe: DataFrame

    def __init__(self) -> None:
        self.dataframe = None

    def analyse(self, data) -> None:
        self.dataframe = DataFrame(data)

    def read_excel(self, file: FileStorage) -> None:
        self.dataframe = DataFrame(read_excel(file).dropna())

    def read_csv(self, file: FileStorage) -> None:
        self.dataframe = DataFrame(read_csv(file).dropna())

    def get_columns(self) -> List[str] | None:
        if self.__has_dataframe():
            return list(self.dataframe.columns)

        return None

    def convert_to_excel(self, folder: str, filename: str) -> None:
        if self.__has_dataframe():
            self.dataframe.to_excel(f"{folder}/{filename}", index=False)

    def convert_to_list_of_records(self) -> List[Dict] | None:
        if self.__has_dataframe():
            return self.dataframe.to_dict("records")

        return None

    def get_data(self):
        return self.dataframe

    def __has_dataframe(self) -> bool:
        return self.dataframe is not None
