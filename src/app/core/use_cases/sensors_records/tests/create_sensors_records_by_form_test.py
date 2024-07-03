from datetime import datetime, date

from pytest import fixture, raises

from core.use_cases.tests.mocks.repositories import (
    SensorRecordsRepositoryMock,
    PlantsRepositoryMock,
)
from core.errors.validation import DatetimeNotValidError, DateNotValidError
from core.errors.plants import PlantNotFoundError
from core.entities.tests.fakers import PlantsFaker


from ..create_sensors_records_by_form import CreateSensorsRecordByForm


def fake_request(base_fake_request: dict):
    return {
        "time": datetime(year=2024, month=12, day=12, hour=12, minute=52),
        "date": date(year=2024, month=12, day=12),
        "soil_humidity": 32,
        "ambient_humidity": 55,
        "temperature": 20,
        "water_volume": 0,
        **base_fake_request,
    }


def describe_create_sensors_record_by_api_use_case():
    @fixture
    def sensors_records_repository():
        return SensorRecordsRepositoryMock()

    @fixture
    def plants_repository():
        return PlantsRepositoryMock()

    @fixture
    def use_case(
        sensors_records_repository: SensorRecordsRepositoryMock,
        plants_repository: PlantsRepositoryMock,
    ):
        return CreateSensorsRecordByForm(
            sensors_records_repository=sensors_records_repository,
            plants_repository=plants_repository,
        )

    def it_should_throw_error_if_time_from_request_is_not_valid(
        use_case: CreateSensorsRecordByForm,
    ):
        request = fake_request({"time": "not valid time"})

        with raises(DatetimeNotValidError):
            use_case.execute(request)

    def it_should_throw_error_if_date_from_request_is_not_valid(
        use_case: CreateSensorsRecordByForm,
    ):
        request = fake_request({"date": "not valid date"})

        with raises(DateNotValidError):
            use_case.execute(request)

    def it_should_throw_error_if_there_is_no_plant_in_repository(
        use_case: CreateSensorsRecordByForm,
    ):
        fake_plant = PlantsFaker.fake()

        request = fake_request({"plant_id": fake_plant.id})

        with raises(PlantNotFoundError):
            use_case.execute(request)

    def it_should_create_sensors_record(
        sensors_records_repository: SensorRecordsRepositoryMock,
        plants_repository: PlantsRepositoryMock,
        use_case: CreateSensorsRecordByForm,
    ):
        fake_plant = PlantsFaker.fake()
        plants_repository.create_plant(fake_plant)

        request = fake_request({"plant_id": fake_plant.id})

        use_case.execute(request)

        last_record = sensors_records_repository.get_last_sensors_records(count=1)[0]

        assert last_record.ambient_humidity == request["ambient_humidity"]
        assert last_record.soil_humidity == request["soil_humidity"]
        assert last_record.temperature == request["temperature"]
        assert last_record.water_volume == request["water_volume"]
        assert last_record.plant == fake_plant
