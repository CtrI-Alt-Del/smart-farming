from datetime import datetime, date

from pytest import fixture, raises

from core.use_cases.tests.mocks.repositories import (
    PlantsRepositoryMock,
    ChecklistRecordsRepositoryMock,
)
from core.entities.tests.fakers import ChecklistRecordsFaker, PlantsFaker
from core.errors.validation import ChecklistRecordNotValidError, DateNotValidError
from core.errors.checklist_records import ChecklistRecordNotFoundError
from core.errors.plants import PlantNotFoundError

from ..update_checklist_record import UpdateChecklistRecord


def fake_request(base_fake_request: dict):
    return {
        "fertilizer_expiration_date": datetime(
            year=2024, month=3, day=16, hour=12, minute=0
        ),
        "date": date(year=2024, month=12, day=12),
        "hour": 12,
        "illuminance": 12,
        "plantation_type": "interno",
        "lai": 55,
        "soil_humidity": 20,
        "air_humidity": 50,
        "temperature": 24.7,
        "water_consumption": 0,
        "soil_ph": 7,
        "report": "não",
        "leaf_color": "avermelhada",
        "leaf_appearance": "um pouco murcha",
        **base_fake_request,
    }


def describe_update_checklist_record_use_case():
    @fixture
    def checklist_records_repository():
        return ChecklistRecordsRepositoryMock()

    @fixture
    def plants_repository():
        return PlantsRepositoryMock()

    @fixture
    def use_case(
        checklist_records_repository: ChecklistRecordsRepositoryMock,
        plants_repository: PlantsRepositoryMock,
    ):
        plants_repository.clear_plants()
        checklist_records_repository.clear_records()
        return UpdateChecklistRecord(
            checklist_records_repository=checklist_records_repository,
            plants_repository=plants_repository,
        )

    def it_should_throw_error_if_id_from_request_is_not_valid(
        use_case: UpdateChecklistRecord,
    ):

        with raises(ChecklistRecordNotValidError):
            use_case.execute(request=fake_request({"checklist_record_id": None}))

    def it_should_throw_error_if_no_checklist_record_is_found_in_repository(
        use_case: UpdateChecklistRecord,
    ):
        fake_record = ChecklistRecordsFaker.fake()

        with raises(ChecklistRecordNotFoundError):
            use_case.execute(
                request=fake_request({"checklist_record_id": fake_record.id})
            )

    def it_should_throw_error_if_date_from_request_is_not_valid(
        checklist_records_repository: ChecklistRecordsRepositoryMock,
        use_case: UpdateChecklistRecord,
    ):
        fake_record = ChecklistRecordsFaker.fake()
        checklist_records_repository.create_checklist_record(fake_record)

        with raises(DateNotValidError):
            use_case.execute(
                request=fake_request(
                    {"checklist_record_id": fake_record.id, "date": None}
                )
            )

    def it_should_throw_error_if_no_plant_is_found_in_repository(
        checklist_records_repository: ChecklistRecordsRepositoryMock,
        use_case: UpdateChecklistRecord,
    ):
        fake_record = ChecklistRecordsFaker.fake()
        checklist_records_repository.create_checklist_record(fake_record)

        fake_plant = PlantsFaker.fake()

        with raises(PlantNotFoundError):
            use_case.execute(
                request=fake_request(
                    {"checklist_record_id": fake_record.id, "plant_id": fake_plant.id}
                )
            )

    def it_should_update_checklist_record(
        checklist_records_repository: ChecklistRecordsRepositoryMock,
        plants_repository: PlantsRepositoryMock,
        use_case: UpdateChecklistRecord,
    ):
        fake_record = ChecklistRecordsFaker.fake(
            soil_humidity=25,
            ambient_humidity=25,
            water_volume=25,
            temperature=25,
        )
        checklist_records_repository.create_checklist_record(fake_record)

        fake_plant = PlantsFaker.fake()
        plants_repository.create_plant(fake_plant)

        request = fake_request(
            {"plant_id": fake_plant.id, "checklist_record_id": fake_record.id}
        )

        use_case.execute(request=request)

        last_record = checklist_records_repository.get_last_checklist_records(count=1)[
            0
        ]

        assert last_record.soil_humidity == request["soil_humidity"]
        assert last_record.soil_ph == request["soil_ph"]
        assert last_record.plantation_type == request["plantation_type"]
        assert last_record.lai == request["lai"]
        assert last_record.illuminance == request["illuminance"]
        assert last_record.leaf_appearance == request["leaf_appearance"]
        assert last_record.leaf_color == request["leaf_color"]
        assert last_record.report == request["report"]
        assert last_record.air_humidity == request["air_humidity"]
        assert last_record.temperature == request["temperature"]
        assert last_record.water_consumption == request["water_consumption"]
        assert (
            last_record.fertilizer_expiration_date.get_value(is_date=True)
            == request["fertilizer_expiration_date"]
        )
        assert (
            last_record.created_at.get_value(is_datetime=True).date() == request["date"]
        )
        assert last_record.plant == fake_plant
