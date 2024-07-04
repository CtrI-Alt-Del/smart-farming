from abc import ABC, abstractmethod
from werkzeug.datastructures import FileStorage


class DataAnalyserProviderInterface(ABC):
    @abstractmethod
    def analyse(self, data) -> None: ...

    @abstractmethod
    def read_excel(self, file: FileStorage) -> None: ...

    @abstractmethod
    def read_csv(self, file: FileStorage) -> None: ...

    @abstractmethod
    def get_columns(self) -> list[str] | None: ...

    @abstractmethod
    def convert_to_excel(self, folder: str, filename: str) -> None: ...

    @abstractmethod
    def convert_to_list_of_records(self) -> list[dict] | None: ...

    @abstractmethod
    def get_data(self): ...
