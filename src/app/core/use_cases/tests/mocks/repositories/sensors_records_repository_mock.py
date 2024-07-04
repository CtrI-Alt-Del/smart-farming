from datetime import date

from core.entities import SensorsRecord
from core.interfaces.repositories import SensorRecordsRepositoryInterface
from core.entities.tests.fakers import LineChartRecordsFaker

from core.constants import PAGINATION


class SensorRecordsRepositoryMock(SensorRecordsRepositoryInterface):
    _sensors_records = []

    def create_sensors_record(self, sensors_record: SensorsRecord) -> None:
        self._sensors_records.append(sensors_record)

    def create_many_sensors_records(self, sensors_records: list[SensorsRecord]):
        for record in sensors_records:
            self._sensors_records.append(record)

    def get_sensor_records_for_line_charts(self):
        return {
            "soil_humidity_line_chart_records": LineChartRecordsFaker.fake_many(),
            "ambient_humidity_line_chart_records": LineChartRecordsFaker.fake_many(),
            "temperature_line_chart_records": LineChartRecordsFaker.fake_many(),
            "water_volume_line_chart_records": LineChartRecordsFaker.fake_many(),
        }

    def get_last_sensors_records(self, count) -> list[SensorsRecord]:
        records = self._sensors_records.copy()

        return records[:count]

    def get_sensors_record_by_id(self, id: str) -> SensorsRecord | None:
        sensors_records = list(
            filter(lambda plant: plant.id == id, self._sensors_records)
        )

        if len(sensors_records):
            return sensors_records[0]

        return None

    def get_sensors_records_count(
        self, plant_id: str, start_date: date, end_date: date, page_number: int = 1
    ) -> int:
        return len(self._sensors_records)

    def update_sensors_record_by_id(self, sensors_record: SensorsRecord):
        self._sensors_records = [
            (
                sensors_record
                if sensors_record.id == current_sensors_record.id
                else current_sensors_record
            )
            for current_sensors_record in self._sensors_records
        ]

    def delete_sensors_record_by_id(self, id: str):
        self._sensors_records = [
            sensors_record
            for sensors_record in self._sensors_records
            if sensors_record.id != id
        ]

    def delete_many_sensors_records_by_id(self, ids: str):
        self._sensors_records = [
            sensors_record
            for sensors_record in self._sensors_records
            if sensors_record.id not in ids
        ]

    def get_filtered_sensors_records(
        self, plant_id: str, start_date: date, end_date: date, page_number: int = 1
    ) -> list[SensorsRecord]:
        records = self._sensors_records

        if plant_id:
            records = [record for record in records if record.plant.id == plant_id]

        if start_date and end_date:
            records = [
                record
                for record in records
                if record.created_at.get_value(is_datetime=True).date() >= start_date
                and record.created_at.get_value(is_datetime=True).date() <= end_date
            ]

        if page_number != "all":
            records_per_page = PAGINATION["records_per_page"]

            slice_start = (page_number - 1) * records_per_page
            records = records[slice_start : slice_start + records_per_page]
        else:
            records = records

        return records

    def clear_records(self):
        self._sensors_records = []
