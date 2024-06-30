from pytest import fixture

from core.use_cases.plants import GetPlantsPageData
from core.use_cases.tests.mocks.repositories import (
    PlantsRepositoryMock,
)
from core.entities.tests.fakers import PlantsFaker


def describe_get_plants_page_data_use_case():
    @fixture
    def repository():
        return PlantsRepositoryMock()

    @fixture
    def use_case(repository):
        repository.clear_plants()

        return GetPlantsPageData(repository)

    def it_should_get_plants(
        repository: PlantsRepositoryMock,
        use_case: GetPlantsPageData,
    ):
        fake_plants = PlantsFaker.fake_many()

        for fake_plant in fake_plants:
            repository.create_plant(fake_plant)

        plants = use_case.execute()

        assert plants == fake_plants
