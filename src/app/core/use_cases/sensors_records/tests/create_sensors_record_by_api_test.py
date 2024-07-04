from dataclasses import asdict

from pytest import fixture, raises

from core.use_cases.tests.mocks.repositories import (
    PlantsRepositoryMock,
    UsersRepositoryMock,
    SensorRecordsRepositoryMock,
)
from core.errors.validation import SensorsRecordNotValidError
from core.errors.plants import PlantNotFoundError
from core.entities.tests.fakers import SensorsRecordsFaker, UsersFaker, PlantsFaker
from core.constants import ADMIN_USER_EMAIL

from ..create_sensors_record_by_api import CreateSensorsRecordByApi


def describe_create_sensors_record_by_api_use_case():
    @fixture
    def plants_repository():
        return PlantsRepositoryMock()

    @fixture
    def users_repository():
        return UsersRepositoryMock()

    @fixture
    def sensors_records_repository():
        return SensorRecordsRepositoryMock()

    @fixture
    def use_case(
        sensors_records_repository: SensorRecordsRepositoryMock,
        plants_repository: PlantsRepositoryMock,
        users_repository: UsersRepositoryMock,
    ):
        users_repository.clear_users()
        plants_repository.clear_plants()
        sensors_records_repository.clear_records()
        return CreateSensorsRecordByApi(
            sensors_records_repository=sensors_records_repository,
            plants_repository=plants_repository,
            users_repository=users_repository,
        )

    @fixture
    def fake_request():
        return asdict(SensorsRecordsFaker.fake())

    def it_should_throw_error_if_request_is_invalid(
        use_case: CreateSensorsRecordByApi,
    ):
        with raises(SensorsRecordNotValidError):
            use_case.execute(None)

    def it_should_throw_error_if_no_active_plant_is_found(
        fake_request,
        use_case: CreateSensorsRecordByApi,
    ):
        with raises(PlantNotFoundError):
            use_case.execute(fake_request)

    def it_should_throw_error_no_active_plant_is_found(
        fake_request,
        users_repository: UsersRepositoryMock,
        sensors_records_repository: SensorRecordsRepositoryMock,
        use_case: CreateSensorsRecordByApi,
    ):
        fake_user = UsersFaker.fake()
        fake_plant = PlantsFaker.fake()
        fake_user.email = ADMIN_USER_EMAIL
        fake_user.active_plant_id = fake_plant.id

        users_repository.create_user(fake_user)

        use_case.execute(fake_request)

        last_record = sensors_records_repository.get_last_sensors_records(count=1)[0]

        assert fake_request["soil_humidity"] == last_record.soil_humidity
        assert fake_request["ambient_humidity"] == last_record.ambient_humidity
        assert fake_request["temperature"] == last_record.temperature
        assert fake_request["water_volume"] == last_record.water_volume
