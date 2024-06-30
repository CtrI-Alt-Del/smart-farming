from pytest import fixture, raises

from core.use_cases.plants import UpdatePlant
from core.commons import Error
from core.use_cases.tests.mocks.repositories import (
    PlantsRepositoryMock,
)
from core.entities.tests.fakers import PlantsFaker


def describe_update_plant_use_case():
    @fixture
    def repository():
        return PlantsRepositoryMock()

    @fixture
    def use_case(repository):
        return UpdatePlant(repository)

    def it_should_throw_an_error_if_id_is_not_string(
        use_case: UpdatePlant,
    ):
        with raises(Error) as error:
            use_case.execute(id=42, request=None)

        assert str(error.value) == "Planta inválida"

    def it_should_throw_an_error_if_plant_does_not_exist(
        use_case: UpdatePlant,
    ):
        fake_plant = PlantsFaker.fake()

        with raises(Error) as error:
            use_case.execute(id=fake_plant.id, request=None)

        assert str(error.value) == "Planta não encontrada"

    def it_should_update_plant(
        repository: PlantsRepositoryMock,
        use_case: UpdatePlant,
    ):
        fake_plant = PlantsFaker.fake()
        repository.create_plant(fake_plant)

        request = {"name": "Updated plant name", "hex_color": "Updated plant hex color"}

        use_case.execute(id=fake_plant.id, request=request)

        created_plant = repository.get_last_plant()

        assert created_plant.name == request["name"]
        assert created_plant.hex_color == request["hex_color"]
