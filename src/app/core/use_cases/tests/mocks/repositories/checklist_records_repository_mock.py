from datetime import date

from core.entities import CheckListRecord
from core.interfaces.repositories import ChecklistRecordsRepositoryInterface
from core.entities.tests.fakers import LineChartRecordsFaker

from core.constants import PAGINATION


class ChecklistRecordsRepositoryMock(ChecklistRecordsRepositoryInterface):
    _checklist_records = []

    def create_checklist_record(self, checklist_record: CheckListRecord) -> None:
        self._checklist_records.append(checklist_record)

    def create_many_checklist_records(self, checklist_records: list[CheckListRecord]):
        for record in checklist_records:
            self._checklist_records.append(record)

    def get_lai_records_for_line_charts(self):
        return LineChartRecordsFaker.fake_many()

    def get_checklist_record_by_id(self, id: str) -> CheckListRecord | None:
        checklist_records = list(
            filter(lambda plant: plant.id == id, self._checklist_records)
        )

        if len(checklist_records):
            return checklist_records[0]

        return None

    def get_checklist_records_count(
        self, plant_id: str, start_date: date, end_date: date
    ):
        return len(self._checklist_records)

    def get_last_checklist_records(self, count) -> list[CheckListRecord]:
        records = self._checklist_records.copy()

        return records[:count]

    def get_leaf_appearances_and_leaf_colors_records(self):
        records = [
            {
                "leaf_appearance": record.leaf_appearance,
                "leaf_color": record.leaf_color,
                "created_at": record.created_at,
                "plant_id": record.plant.id,
            }
            for record in self._checklist_records
        ]

        records.sort(
            key=lambda record: record["created_at"].get_value(is_datetime=True)
        )

        return records

    def update_checklist_record_by_id(self, checklist_record: CheckListRecord):
        self._checklist_records = [
            (
                checklist_record
                if checklist_record.id == current_checklist_record.id
                else current_checklist_record
            )
            for current_checklist_record in self._checklist_records
        ]

    def delete_checklist_record_by_id(self, id: str):
        self._checklist_records = [
            checklist_record
            for checklist_record in self._checklist_records
            if checklist_record.id != id
        ]

    def delete_many_checklist_records_by_id(self, ids: str):
        self._checklist_records = [
            checklist_record
            for checklist_record in self._checklist_records
            if checklist_record.id not in ids
        ]

    def get_filtered_checklist_records(
        self, plant_id: str, start_date: date, end_date: date, page_number: int = 1
    ) -> list[CheckListRecord]:
        records = self._checklist_records

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

        records.sort(key=lambda record: record.created_at.get_value(is_datetime=True))

        return records

    def clear_records(self):
        self._checklist_records = []
