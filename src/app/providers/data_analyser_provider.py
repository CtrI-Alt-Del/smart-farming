from typing import List, Dict

from pandas import DataFrame, read_csv, read_excel


class DataAnalyserProvider:
    dataframe: DataFrame

    def __init__(self) -> None:
        self.dataframe = None

    def analyse(self, data) -> None:
        self.dataframe = data

    def read_csv(self) -> None:
        if self.__has_dataframe():
            self.dataframe = read_csv(self.dataframe).dropna()

    def read_excel(self) -> None:
        if self.__has_dataframe():
            self.dataframe = read_excel(self.dataframe).dropna()

    def convert_to_list_of_records(self) -> List[Dict] | None:
        if self.__has_dataframe():
            return self.dataframe.to_dict("records")

        return None

    def __has_dataframe(self) -> bool:
        return self.dataframe is not None
