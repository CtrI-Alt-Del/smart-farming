from pytest import fixture, raises

from core.use_cases.tests.mocks.repositories import (
    PlantsRepositoryMock,
    UsersRepositoryMock,
    ChecklistRecordsRepositoryMock,
)
from core.entities import User, Plant
from core.entities.tests.fakers import PlantsFaker, UsersFaker, ChecklistRecordsFaker
from core.commons import OrderedPlants
from core.errors.checklist_records import ChecklistRecordNotFoundError
from core.errors.plants import PlantNotFoundError
from core.constants import ADMIN_USER_EMAIL

from ..get_checklist_records_dashboard_page_data import (
    GetChecklistRecordsDashboardPageData,
)


def describe_get_checklist_records_dashboard_page_data_use_case():
    @fixture
    def plants_repository():
        return PlantsRepositoryMock()

    @fixture
    def users_repository():
        return UsersRepositoryMock()

    @fixture
    def checklist_records_repository():
        return ChecklistRecordsRepositoryMock()

    @fixture
    def use_case(
        checklist_records_repository: ChecklistRecordsRepositoryMock,
        plants_repository: PlantsRepositoryMock,
        users_repository: UsersRepositoryMock,
    ):
        plants_repository.clear_plants()
        users_repository.clear_users()
        return GetChecklistRecordsDashboardPageData(
            checklist_records_repository=checklist_records_repository,
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
        use_case: GetChecklistRecordsDashboardPageData,
    ):
        with raises(PlantNotFoundError):
            use_case.execute()

    def it_should_throw_error_if_there_is_no_checklist_record_in_repository(
        plants_repository: PlantsRepositoryMock,
        users_repository: UsersRepositoryMock,
        checklist_records_repository: ChecklistRecordsRepositoryMock,
        fake_user: User,
        fake_plant: Plant,
        use_case: GetChecklistRecordsDashboardPageData,
    ):
        users_repository.create_user(fake_user)
        plants_repository.create_plant(fake_plant)

        checklist_records_repository.get_sensor_records_for_line_charts = lambda: []

        with raises(ChecklistRecordNotFoundError):
            use_case.execute()

    def it_should_get_data_for_leaf_apprearance_and_plant_chart(
        plants_repository: PlantsRepositoryMock,
        users_repository: UsersRepositoryMock,
        checklist_records_repository: ChecklistRecordsRepositoryMock,
        fake_user: User,
        fake_plant: Plant,
        use_case: GetChecklistRecordsDashboardPageData,
    ):
        users_repository.create_user(fake_user)
        plants_repository.create_plant(fake_plant)

        fake_records = [
            ChecklistRecordsFaker.fake(leaf_appearance="SAUDAVEL", plant=fake_plant),
            ChecklistRecordsFaker.fake(leaf_appearance="SAUDAVEL", plant=fake_plant),
            ChecklistRecordsFaker.fake(leaf_appearance="MURCHA", plant=fake_plant),
        ]

        checklist_records_repository.create_many_checklist_records(fake_records)

        data = use_case.execute()

        chart_data = data["days_count_by_leaf_appearance_and_plant"][fake_plant.id]

        assert chart_data["SAUDAVEL"] == 2
        assert chart_data["MURCHA"] == 1
        assert chart_data["NÃO REGISTRADO"] == 0

    def it_should_get_data_for_leaf_color_and_plant_chart(
        plants_repository: PlantsRepositoryMock,
        users_repository: UsersRepositoryMock,
        checklist_records_repository: ChecklistRecordsRepositoryMock,
        fake_user: User,
        fake_plant: Plant,
        use_case: GetChecklistRecordsDashboardPageData,
    ):
        users_repository.create_user(fake_user)
        plants_repository.create_plant(fake_plant)

        fake_records = [
            ChecklistRecordsFaker.fake(
                leaf_color="VERDE CLARO PREDOMINANTE", plant=fake_plant
            ),
            ChecklistRecordsFaker.fake(
                leaf_color="VERDE ESCURO PREDOMINANTE", plant=fake_plant
            ),
            ChecklistRecordsFaker.fake(
                leaf_color="VERDE ESCURO PREDOMINANTE", plant=fake_plant
            ),
            ChecklistRecordsFaker.fake(leaf_color="NÃO REGISTRADO", plant=fake_plant),
        ]

        checklist_records_repository.create_many_checklist_records(fake_records)

        data = use_case.execute()

        chart_data = data["days_count_by_leaf_color_and_plant"][fake_plant.id]

        assert chart_data["VERDE CLARO PREDOMINANTE"] == 1
        assert chart_data["VERDE ESCURO PREDOMINANTE"] == 2
        assert chart_data["NÃO REGISTRADO"] == 1
        assert chart_data["VERDE CLARO COM ALGUMAS MANCHAS CLARAS"] == 0
        assert chart_data["VERDE CLARO COM VARIAS MANCHAS CLARAS"] == 0
        assert chart_data["VERDE CLARO COM ALGUMAS MANCHAS ESCURAS"] == 0
        assert chart_data["VERDE CLARO COM VARIAS MANCHAS ESCURAS"] == 0
        assert chart_data["VERDE ESCURO COM ALGUMAS MANCHAS CLARAS"] == 0
        assert chart_data["VERDE ESCURO COM VARIAS MANCHAS CLARAS"] == 0
        assert chart_data["VERDE ESCURO COM ALGUMAS MANCHAS ESCURAS"] == 0
        assert chart_data["VERDE ESCURO COM VARIAS MANCHAS ESCURAS"] == 0
        assert chart_data["OPACO PREDOMINANTE"] == 0

    def it_should_get_ordered_plants(
        plants_repository: PlantsRepositoryMock,
        users_repository: UsersRepositoryMock,
        fake_user: User,
        fake_plant: Plant,
        use_case: GetChecklistRecordsDashboardPageData,
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
        use_case: GetChecklistRecordsDashboardPageData,
    ):
        users_repository.create_user(fake_user)

        fake_plants = PlantsFaker.fake_many(2)
        fake_plants.append(fake_plant)

        for plant in fake_plants:
            plants_repository.create_plant(plant)

        data = use_case.execute()

        assert data["active_plant_id"] == fake_user.active_plant_id
