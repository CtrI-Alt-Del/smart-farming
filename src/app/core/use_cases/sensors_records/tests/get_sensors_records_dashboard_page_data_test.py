from pytest import fixture, raises

from core.use_cases.tests.mocks.repositories import (
    PlantsRepositoryMock,
    UsersRepositoryMock,
    SensorRecordsRepositoryMock,
)
from core.entities import User, Plant
from core.entities.tests.fakers import PlantsFaker, UsersFaker
from core.commons import OrderedPlants
from core.errors.sensors_records import SensorsRecordNotFoundError
from core.errors.plants import PlantNotFoundError
from core.constants import ADMIN_USER_EMAIL

from ..get_sensors_records_dashboard_page_data import GetSensorsRecordsDashboardPageData


def describe_get_sensors_records_dashboard_page_data_use_case():
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
        plants_repository.clear_plants()
        users_repository.clear_users()
        return GetSensorsRecordsDashboardPageData(
            sensors_records_repository=sensors_records_repository,
            plants_repository=plants_repository,
            users_repository=users_repository,
        )

    @fixture
    def fake_plant():
        return PlantsFaker.fake()

    @fixture
    def fake_user(fake_plant):
        fake_user = UsersFaker.fake(email=ADMIN_USER_EMAIL)
        fake_user.active_plant_id = fake_plant.id
        return fake_user

    def it_should_throw_error_if_there_is_no_plant_in_repository(
        use_case: GetSensorsRecordsDashboardPageData,
    ):
        with raises(PlantNotFoundError) as error:
            use_case.execute()

        assert str(error.value) == "Nenhuma planta encontrada"

    def it_should_throw_error_if_there_is_no_sensors_record_in_repository(
        plants_repository: PlantsRepositoryMock,
        users_repository: UsersRepositoryMock,
        sensors_records_repository: SensorRecordsRepositoryMock,
        fake_user: User,
        fake_plant: Plant,
        use_case: GetSensorsRecordsDashboardPageData,
    ):
        users_repository.create_user(fake_user)
        plants_repository.create_plant(fake_plant)

        sensors_records_repository.get_sensor_records_for_line_charts = lambda: []

        with raises(SensorsRecordNotFoundError) as error:
            use_case.execute()

        assert str(error.value) == "Nenhum registro dos sensores encontrado"

    def it_should_get_data_for_each_line_chart(
        plants_repository: PlantsRepositoryMock,
        users_repository: UsersRepositoryMock,
        fake_user: User,
        fake_plant: Plant,
        use_case: GetSensorsRecordsDashboardPageData,
    ):
        users_repository.create_user(fake_user)
        plants_repository.create_plant(fake_plant)

        data = use_case.execute()

        assert isinstance(data["soil_humidity_chart_data"], dict)
        assert isinstance(data["ambient_humidity_chart_data"], dict)
        assert isinstance(data["temperature_chart_data"], dict)
        assert isinstance(data["water_volume_chart_data"], dict)

    def it_should_get_ordered_plants(
        plants_repository: PlantsRepositoryMock,
        users_repository: UsersRepositoryMock,
        fake_user: User,
        fake_plant: Plant,
        use_case: GetSensorsRecordsDashboardPageData,
    ):
        users_repository.create_user(fake_user)

        fake_plants = PlantsFaker.fake_many(2)
        fake_plants.append(fake_plant)

        for plant in fake_plants:
            plants_repository.create_plant(plant)

        data = use_case.execute()

        assert (
            data["plants"]
            == OrderedPlants(fake_plants, fake_user.active_plant_id).get_value()
        )

    def it_should_get_active_plant_id(
        plants_repository: PlantsRepositoryMock,
        users_repository: UsersRepositoryMock,
        fake_user: User,
        fake_plant: Plant,
        use_case: GetSensorsRecordsDashboardPageData,
    ):
        users_repository.create_user(fake_user)

        fake_plants = PlantsFaker.fake_many(2)
        fake_plants.append(fake_plant)

        for plant in fake_plants:
            plants_repository.create_plant(plant)

        data = use_case.execute()

        assert data["active_plant_id"] == fake_user.active_plant_id
