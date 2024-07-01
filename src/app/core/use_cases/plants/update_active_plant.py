from core.interfaces.repositories import (
    PlantsRepositoryInterface,
    UsersRepositoryInterface,
)
from core.entities import Plant
from core.errors.authentication import UserNotValidError
from core.errors.plants import PlantIdNotValidError, PlantNotFoundError


class UpdateActivePlant:
    def __init__(
        self,
        plants_repository: PlantsRepositoryInterface,
        users_repository: UsersRepositoryInterface,
    ):
        self.plants_repository = plants_repository
        self.users_repository = users_repository

    def execute(self, user_id: str, plant_id: str):
        if not isinstance(user_id, str):
            raise UserNotValidError()

        if not isinstance(plant_id, str):
            raise PlantIdNotValidError()

        plant = self.plants_repository.get_plant_by_id(plant_id)

        if not isinstance(plant, Plant):
            raise PlantNotFoundError

        self.users_repository.update_active_plant(user_id, plant_id)
