from datetime import datetime, date

from pytest import fixture, raises

from core.use_cases.tests.mocks.repositories import (
    PlantsRepositoryMock,
    SensorRecordsRepositoryMock,
)
from core.entities.tests.fakers import SensorsRecordsFaker, PlantsFaker
from core.errors.validation import SensorsRecordNotValidError, DatetimeNotValidError
from core.errors.sensors_records import SensorsRecordNotFoundError
from core.errors.plants import PlantNotFoundError

from ..update_sensors_record import UpdateSensorsRecord


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


def describe_update_sensors_record_use_case():
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
        plants_repository.clear_plants()
        sensors_records_repository.clear_records()
        return UpdateSensorsRecord(
            sensors_records_repository=sensors_records_repository,
            plants_repository=plants_repository,
        )

    def it_should_throw_error_if_id_from_request_is_not_valid(
        use_case: UpdateSensorsRecord,
    ):

        with raises(SensorsRecordNotValidError):
            use_case.execute(request=fake_request({"sensors_record_id": None}))

    def it_should_throw_error_if_no_sensors_record_is_found_in_repository(
        use_case: UpdateSensorsRecord,
    ):
        fake_record = SensorsRecordsFaker.fake()

        with raises(SensorsRecordNotFoundError):
            use_case.execute(
                request=fake_request({"sensors_record_id": fake_record.id})
            )

    def it_should_throw_error_if_date_from_request_is_not_valid(
        sensors_records_repository: SensorRecordsRepositoryMock,
        use_case: UpdateSensorsRecord,
    ):
        fake_record = SensorsRecordsFaker.fake()
        sensors_records_repository.create_sensors_record(fake_record)

        with raises(DatetimeNotValidError):
            use_case.execute(
                request=fake_request(
                    {"sensors_record_id": fake_record.id, "date": None}
                )
            )

    def it_should_throw_error_if_no_plant_is_found_in_repository(
        sensors_records_repository: SensorRecordsRepositoryMock,
        use_case: UpdateSensorsRecord,
    ):
        fake_record = SensorsRecordsFaker.fake()
        sensors_records_repository.create_sensors_record(fake_record)

        fake_plant = PlantsFaker.fake()

        with raises(PlantNotFoundError):
            use_case.execute(
                request=fake_request(
                    {"sensors_record_id": fake_record.id, "plant_id": fake_plant.id}
                )
            )

    def it_should_update_sensors_record(
        sensors_records_repository: SensorRecordsRepositoryMock,
        plants_repository: PlantsRepositoryMock,
        use_case: UpdateSensorsRecord,
    ):
        fake_record = SensorsRecordsFaker.fake(
            soil_humidity=25,
            ambient_humidity=25,
            water_volume=25,
            temperature=25,
        )
        sensors_records_repository.create_sensors_record(fake_record)

        fake_plant = PlantsFaker.fake()
        plants_repository.create_plant(fake_plant)

        request = fake_request(
            {
                "sensors_record_id": fake_record.id,
                "soil_humidity": 0,
                "ambient_humidity": 0,
                "temperature": 0,
                "water_volume": 0,
                "plant_id": fake_plant.id,
            }
        )

        use_case.execute(request=request)

        last_record = sensors_records_repository.get_last_sensors_records(count=1)[0]

        assert last_record.ambient_humidity == request["ambient_humidity"]
        assert last_record.soil_humidity == request["soil_humidity"]
        assert last_record.temperature == request["temperature"]
        assert last_record.water_volume == request["water_volume"]
        assert last_record.plant.id == fake_plant.id
