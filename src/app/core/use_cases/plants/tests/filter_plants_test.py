from pytest import fixture, raises

from core.use_cases.plants import FilterPlants
from core.commons import Error
from core.use_cases.tests.mocks.repositories import (
    PlantsRepositoryMock,
)
from core.entities.tests.fakers import PlantsFaker


def describe_filter_plants_use_case():
    @fixture
    def repository():
        return PlantsRepositoryMock()

    @fixture
    def use_case(repository):
        repository.clear_plants()

        return FilterPlants(repository)

    def it_should_throw_an_error_if_plant_name_is_not_string(
        use_case: FilterPlants,
    ):
        with raises(Error) as error:
            use_case.execute(plant_name=42)

        assert str(error.value) == "Nome de planta inválida"

    def it_should_not_filter_plants_if_provided_name_is_empty(
        use_case: FilterPlants,
    ):
        filtered_plants = use_case.execute(plant_name="")

        assert len(filtered_plants) == 0

    def it_should_filter_plants(
        use_case: FilterPlants, repository: PlantsRepositoryMock
    ):
        fake_name = "doce"

        repository.create_plant(PlantsFaker.fake(name="batata doce"))
        repository.create_plant(PlantsFaker.fake(name="alface"))
        repository.create_plant(PlantsFaker.fake(name="doce"))

        filtered_plants = use_case.execute(plant_name=fake_name)

        assert len(filtered_plants) == 2
        assert all([fake_name in plant.name for plant in filtered_plants])
