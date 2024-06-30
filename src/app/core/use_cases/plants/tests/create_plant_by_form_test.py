from dataclasses import asdict

from pytest import fixture, raises

from core.use_cases.plants.create_plant_by_form import CreatePlantByForm
from core.commons.error import Error

from core.use_cases.tests.mocks.repositories import (
    PlantsRepositoryMock,
)
from core.entities.tests.fakers import PlantsFaker


def describe_create_plant_by_form_use_case():
    @fixture
    def repository():
        repository = PlantsRepositoryMock()

        yield repository

        repository.clear_plants()

    @fixture
    def use_case(repository):
        return CreatePlantByForm(repository)

    def it_should_throw_an_error_if_the_new_plant_name_is_already_in_use(
        repository: PlantsRepositoryMock,
        use_case: CreatePlantByForm,
    ):
        fake_plant = PlantsFaker.fake()

        repository.create_plant(fake_plant)

        with raises(Error) as error:
            use_case.execute(request=asdict(fake_plant))

        assert str(error.value) == "Nome de planta já utilizada"

    def it_should_create_a_plant(
        repository: PlantsRepositoryMock,
        use_case: CreatePlantByForm,
    ):
        fake_plant = PlantsFaker.fake()

        use_case.execute(request=asdict(fake_plant))

        created_plant = repository.get_last_plant()

        assert created_plant.name == fake_plant.name
        assert created_plant.hex_color == fake_plant.hex_color
