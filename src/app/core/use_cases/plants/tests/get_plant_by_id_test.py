from pytest import fixture, raises

from core.use_cases.plants import GetPlantById
from core.use_cases.tests.mocks.repositories import (
    PlantsRepositoryMock,
)
from core.entities.tests.fakers import PlantsFaker
from core.errors.plants import PlantIdNotValidError


def describe_get_plant_by_id_use_case():
    @fixture
    def repository():
        return PlantsRepositoryMock()

    @fixture
    def use_case(repository):
        return GetPlantById(repository)

    def it_should_throw_an_error_if_plant_id_is_not_valid(
        use_case: GetPlantById,
    ):
        with raises(PlantIdNotValidError):
            use_case.execute(42)

    def it_should_get_plant(
        repository: PlantsRepositoryMock,
        use_case: GetPlantById,
    ):
        fake_plant = PlantsFaker.fake()

        repository.create_plant(fake_plant)

        plant = use_case.execute(fake_plant.id)

        assert plant == fake_plant
