from pytest import fixture, raises

from core.use_cases.plants import GetPlantById
from core.commons import Error
from core.use_cases.tests.mocks.repositories import (
    PlantsRepositoryMock,
)
from core.entities.tests.fakers import PlantsFaker


def describe_get_plant_by_id_use_case():
    @fixture
    def repository():
        return PlantsRepositoryMock()

    @fixture
    def use_case(repository):
        return GetPlantById(repository)

    def it_should_throw_an_error_if_plant_id_is_not_string(
        use_case: GetPlantById,
    ):
        with raises(Error) as error:
            use_case.execute(42)

        assert str(error.value) == "Planta inválida"

    def it_should_get_plant(
        repository: PlantsRepositoryMock,
        use_case: GetPlantById,
    ):
        fake_plant = PlantsFaker.fake()

        repository.create_plant(fake_plant)

        plant = use_case.execute(fake_plant.id)

        assert plant == fake_plant
