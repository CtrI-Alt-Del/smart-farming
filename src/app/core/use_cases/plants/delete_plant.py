from core.entities import User
from core.errors.plants import PlantIdNotValidError, PlantNotFoundError
from core.errors.authentication import UserNotValidError
from core.interfaces.repositories import (
    PlantsRepositoryInterface,
    UsersRepositoryInterface,
)


class DeletePlant:
    def __init__(
        self,
        plants_repository: PlantsRepositoryInterface,
        users_repository: UsersRepositoryInterface,
    ):
        self.plants_repository = plants_repository
        self.users_repository = users_repository

    def execute(self, user: User, plant_id: str):
        print(plant_id)
        if not isinstance(plant_id, str):
            raise PlantIdNotValidError()

        if not isinstance(user, User):
            raise UserNotValidError()

        has_plant = bool(self.plants_repository.get_plant_by_id(plant_id))

        if not has_plant:
            raise PlantNotFoundError()

        self.plants_repository.delete_plant_by_id(plant_id)

        if user.active_plant_id == plant_id:
            last_plant = self.plants_repository.get_last_plant()
            if last_plant:
                self.users_repository.update_active_plant(user.id, last_plant.id)
