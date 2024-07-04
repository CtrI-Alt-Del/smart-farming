from abc import ABC, abstractmethod
from datetime import date

from core.entities import CheckListRecord, LineChartRecord


class ChecklistRecordsRepositoryInterface(ABC):
    @abstractmethod
    def create_checklist_record(self, checklist_record: CheckListRecord): ...

    @abstractmethod
    def create_many_checklist_records(
        self, checklist_records: list[CheckListRecord]
    ) -> None: ...

    @abstractmethod
    def delete_checklist_record_by_id(self, id: str) -> None: ...

    @abstractmethod
    def delete_many_checklist_records_by_id(self, ids: list[str]) -> None: ...

    @abstractmethod
    def get_filtered_checklist_records(
        self, plant_id: str, start_date: date, end_date: date, page_number: int = 1
    ) -> list[CheckListRecord]: ...

    @abstractmethod
    def get_leaf_appearances_and_leaf_colors_records(self) -> list[dict]: ...

    @abstractmethod
    def get_lai_records_for_line_charts(self) -> list[LineChartRecord]: ...

    @abstractmethod
    def get_checklist_records_count(
        self, plant_id: str, start_date: date, end_date: date
    ) -> int: ...

    @abstractmethod
    def get_checklist_record_by_id(self, id: str) -> CheckListRecord | None: ...
