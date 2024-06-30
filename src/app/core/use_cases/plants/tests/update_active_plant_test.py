from pytest import fixture, raises

from core.use_cases.plants import UpdateActivePlant
from core.commons import Error
from core.use_cases.tests.mocks.repositories import (
    PlantsRepositoryMock,
    UsersRepositoryMock,
)
from core.entities.tests.fakers import PlantsFaker, UsersFaker


def describe_update_active_plant_use_case():
    @fixture
    def plants_repository():
        return PlantsRepositoryMock()

    @fixture
    def users_repository():
        return UsersRepositoryMock()

    @fixture
    def use_case(plants_repository, users_repository):
        return UpdateActivePlant(
            plants_repository=plants_repository, users_repository=users_repository
        )

    def it_should_throw_an_error_if_user_id_is_not_valid(
        use_case: UpdateActivePlant,
    ):
        with raises(Error) as error:
            use_case.execute(user_id=42, plant_id=None)

        assert str(error.value) == "Usuário inválido"

    def it_should_throw_an_error_if_plant_id_is_not_valid(
        use_case: UpdateActivePlant,
    ):
        fake_user = UsersFaker.fake()

        with raises(Error) as error:
            use_case.execute(user_id=fake_user.id, plant_id=None)

        assert str(error.value) == "Planta inválida"

    def it_should_throw_an_error_if_no_plant_is_found(
        use_case: UpdateActivePlant,
    ):
        fake_user = UsersFaker.fake()
        fake_plant = PlantsFaker.fake()

        with raises(Error) as error:
            use_case.execute(user_id=fake_user.id, plant_id=fake_plant.id)

        assert str(error.value) == "Planta não encontrada"

    def it_should_update_active_plant(
        plants_repository: PlantsRepositoryMock,
        users_repository: UsersRepositoryMock,
        use_case: UpdateActivePlant,
    ):
        fake_user = UsersFaker.fake()
        fake_plant = PlantsFaker.fake()

        users_repository.create_user(fake_user)
        plants_repository.create_plant(fake_plant)

        use_case.execute(user_id=fake_user.id, plant_id=fake_plant.id)

        assert fake_user.active_plant_id == fake_plant.id
