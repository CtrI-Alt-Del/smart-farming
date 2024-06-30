from core.commons import Error
from core.entities import User
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
        try:

            print(plant_id)
            if not isinstance(plant_id, str):
                raise Error(
                    ui_message="Id de planta não fornecida",
                    internal_message="Plant id is not provided",
                    status_code=404,
                )

            if not isinstance(user, User):
                raise Error(
                    ui_message="Usuário não fornecido",
                    internal_message="User is not provided",
                    status_code=404,
                )

            has_plant = bool(self.plants_repository.get_plant_by_id(plant_id))

            if not has_plant:
                raise Error(
                    ui_message="Planta não encontrada",
                    internal_message="Plant not found",
                    status_code=404,
                )

            self.plants_repository.delete_plant_by_id(plant_id)

            if user.active_plant_id == plant_id:
                last_plant = self.plants_repository.get_last_plant()
                if last_plant:
                    self.users_repository.update_active_plant(user.id, last_plant.id)

        except Error as error:
            raise error
