from datetime import datetime

from pytest import fixture

from core.use_cases.tests.mocks.repositories import (
    PlantsRepositoryMock,
    ChecklistRecordsRepositoryMock,
)
from core.entities.tests.fakers import PlantsFaker, ChecklistRecordsFaker
from core.commons import Datetime
from core.constants import PAGINATION

from ..get_checklist_records_table_page_data import GetChecklistRecordsTablePageData


def describe_get_checklist_records_dashboard_page_data_use_case():
    @fixture
    def plants_repository():
        return PlantsRepositoryMock()

    @fixture
    def checklist_records_repository():
        return ChecklistRecordsRepositoryMock()

    @fixture
    def use_case(
        checklist_records_repository: ChecklistRecordsRepositoryMock,
        plants_repository: PlantsRepositoryMock,
    ):
        plants_repository.clear_plants()
        checklist_records_repository.clear_records()
        return GetChecklistRecordsTablePageData(
            checklist_records_repository=checklist_records_repository,
            plants_repository=plants_repository,
        )

    def it_should_get_plants_only_when_is_required(
        plants_repository: PlantsRepositoryMock,
        use_case: GetChecklistRecordsTablePageData,
    ):
        fake_plants = PlantsFaker.fake_many()

        for fake_plant in fake_plants:
            plants_repository.create_plant(fake_plant)

        data = use_case.execute(
            should_get_plants=True,
            plant_id=None,
            start_date=None,
            end_date=None,
            page_number=1,
        )

        assert data["plants"] == fake_plants

        data = use_case.execute(
            should_get_plants=False,
            plant_id=None,
            start_date=None,
            end_date=None,
            page_number=1,
        )

        assert data["plants"] == []

    def it_should_get_checklist_records_filtered_by_plant_id(
        checklist_records_repository: ChecklistRecordsRepositoryMock,
        plants_repository: PlantsRepositoryMock,
        use_case: GetChecklistRecordsTablePageData,
    ):
        fake_plant = PlantsFaker.fake()
        plants_repository.create_plant(fake_plant)

        records = ChecklistRecordsFaker.fake_many(5)
        record_in_filter = ChecklistRecordsFaker.fake(plant=fake_plant)

        records.append(record_in_filter)

        checklist_records_repository.create_many_checklist_records(records)

        data = use_case.execute(
            should_get_plants=True,
            plant_id=fake_plant.id,
            start_date=None,
            end_date=None,
            page_number=1,
        )

        data["checklist_records"] == [record_in_filter]

    def it_should_get_checklist_records_filtered_by_date(
        checklist_records_repository: ChecklistRecordsRepositoryMock,
        plants_repository: PlantsRepositoryMock,
        use_case: GetChecklistRecordsTablePageData,
    ):
        fake_plant = PlantsFaker.fake()
        plants_repository.create_plant(fake_plant)

        fake_records = ChecklistRecordsFaker.fake_many(10)

        fake_records.append(
            ChecklistRecordsFaker.fake(
                created_at=Datetime(
                    datetime(year=2024, month=11, day=12, hour=0, minute=0, second=0)
                )
            )
        )

        fake_records_in_filter = []

        fake_records_in_filter.append(
            ChecklistRecordsFaker.fake(
                created_at=Datetime(
                    datetime(year=2024, month=12, day=12, hour=0, minute=0, second=0)
                )
            )
        )
        fake_records_in_filter.append(
            ChecklistRecordsFaker.fake(
                created_at=Datetime(
                    datetime(year=2024, month=12, day=25, hour=0, minute=0, second=0)
                )
            )
        )
        fake_records_in_filter.append(
            ChecklistRecordsFaker.fake(
                created_at=Datetime(
                    datetime(year=2024, month=12, day=30, hour=0, minute=0, second=0)
                )
            )
        )

        fake_records.extend(fake_records_in_filter)

        checklist_records_repository.create_many_checklist_records(fake_records)

        data = use_case.execute(
            should_get_plants=True,
            plant_id=None,
            start_date="2024-12-12",
            end_date="2024-12-30",
            page_number=1,
        )

        assert data["checklist_records"] == fake_records_in_filter

    def it_should_get_checklist_records_filtered_by_page(
        checklist_records_repository: ChecklistRecordsRepositoryMock,
        plants_repository: PlantsRepositoryMock,
        use_case: GetChecklistRecordsTablePageData,
    ):
        fake_plant = PlantsFaker.fake()
        plants_repository.create_plant(fake_plant)

        fake_records = ChecklistRecordsFaker.fake_many(24)

        fake_records.sort(
            key=lambda record: record.created_at.get_value(is_datetime=True)
        )

        checklist_records_repository.create_many_checklist_records(fake_records)

        page_number = 4

        data = use_case.execute(
            should_get_plants=False,
            plant_id=None,
            start_date=None,
            end_date=None,
            page_number=page_number,
        )

        records_per_page = PAGINATION["records_per_page"]
        records_slice = (page_number - 1) * records_per_page

        assert len(data["checklist_records"]) == records_per_page
        assert data["checklist_records"] == fake_records[records_slice:]
