from abc import ABC, abstractmethod
from datetime import date

from core.entities import SensorsRecord, LineChartRecord


class SensorRecordsRepositoryInterface(ABC):
    @abstractmethod
    def create_sensors_record(self, sensors_record: SensorsRecord) -> None: ...

    @abstractmethod
    def create_many_sensors_records(
        self, sensors_records: list[SensorsRecord]
    ) -> None: ...

    @abstractmethod
    def get_sensor_records_for_line_charts(
        self,
    ) -> list[dict[str, LineChartRecord]]: ...

    @abstractmethod
    def get_last_sensors_records(self, count) -> list[SensorsRecord]: ...

    @abstractmethod
    def get_sensors_record_by_id(self, id: str) -> SensorsRecord | None: ...

    @abstractmethod
    def get_sensors_records_count(self) -> int: ...

    @abstractmethod
    def update_sensors_record_by_id(self, sensors_record: SensorsRecord) -> None: ...

    @abstractmethod
    def delete_sensors_record_by_id(self, sensors_record_id: str) -> None: ...

    @abstractmethod
    def delete_many_sensors_records_by_id(self, sensors_record_id: str) -> None: ...

    @abstractmethod
    def get_filtered_sensors_records(
        self, plant_id: str, start_date: date, end_date: date, page_number: int = 1
    ) -> list[SensorsRecord]: ...
