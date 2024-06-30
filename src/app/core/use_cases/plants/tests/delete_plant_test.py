from pytest import fixture, raises

from core.commons.error import Error
from core.use_cases.plants import DeletePlant

from core.use_cases.tests.mocks.repositories import (
    PlantsRepositoryMock,
    UsersRepositoryMock,
)
from core.entities.tests.fakers import PlantsFaker, UsersFaker


def describe_delete_plant_use_case():
    @fixture
    def plants_repository():
        plants_repository = PlantsRepositoryMock()

        yield plants_repository

        plants_repository.clear_plants()

    @fixture
    def users_repository():
        return UsersRepositoryMock()

    @fixture
    def use_case(plants_repository, users_repository):
        plants_repository.clear_plants()

        return DeletePlant(
            plants_repository=plants_repository, users_repository=users_repository
        )

    def it_should_throw_an_error_if_any_plant_id_is_not_provided(
        use_case: DeletePlant,
    ):
        with raises(Error) as error:
            use_case.execute(plant_id=None, user=None)

        assert str(error.value) == "Id de planta não fornecida"

    def it_should_throw_an_error_if_any_user_is_not_provided(
        use_case: DeletePlant,
    ):
        fake_plant = PlantsFaker.fake()

        with raises(Error) as error:
            use_case.execute(plant_id=fake_plant.id, user=None)

        assert str(error.value) == "Usuário não fornecido"

    def it_should_throw_an_error_if_any_plant_is_found(
        use_case: DeletePlant,
    ):
        fake_plant = PlantsFaker.fake()
        fake_user = UsersFaker.fake()

        with raises(Error) as error:
            use_case.execute(plant_id=fake_plant.id, user=fake_user)

        assert str(error.value) == "Planta não encontrada"

    def it_should_delete_plant(
        plants_repository: PlantsRepositoryMock,
        use_case: DeletePlant,
    ):
        fake_plant = PlantsFaker.fake()
        fake_user = UsersFaker.fake()

        plants_repository.create_plant(fake_plant)

        use_case.execute(plant_id=fake_plant.id, user=fake_user)

        plants = plants_repository.get_plants()

        assert len(plants) == 0

    def it_should_set_user_active_plant_id_to_last_plant_id_if_the_deleted_plant_id_was_the_previous_active_plant_of_user(
        plants_repository: PlantsRepositoryMock,
        users_repository: UsersRepositoryMock,
        use_case: DeletePlant,
    ):
        fake_plant = PlantsFaker.fake()
        fake_last_plant = PlantsFaker.fake()

        fake_user = UsersFaker.fake()

        users_repository.create_user(fake_user)

        fake_user.active_plant_id = fake_plant.id

        plants_repository.create_plant(fake_last_plant)
        plants_repository.create_plant(fake_plant)

        use_case.execute(plant_id=fake_plant.id, user=fake_user)

        assert fake_user.active_plant_id == fake_last_plant.id
