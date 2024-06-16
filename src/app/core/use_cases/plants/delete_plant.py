from core.commons import Error
from core.entities import User

from infra.repositories import plants_repository, users_repository


class DeletePlant:
    def execute(self, user: User, plant_id: str) -> None:
        try:
            if not isinstance(plant_id, str):
                raise Error(
                    ui_message="Planta não encontrada",
                    internal_message="Plant id is not provided",
                    status_code=404,
                )

            if not isinstance(user, User):
                raise Error(
                    ui_message="Usuário não encontrada",
                    internal_message="User is not provided",
                    status_code=404,
                )

            has_plant = bool(plants_repository.get_plant_by_id(plant_id))

            if not has_plant:
                raise Error(
                    ui_message="Planta não encontrado",
                    internal_message="Plant not found",
                    status_code=404,
                )

            if user.active_plant_id == plant_id:
                last_plant = plants_repository.get_last_plant()
                if last_plant:
                    users_repository.update_active_plant(user.id, last_plant.id)

            plants_repository.delete_plant_by_id(plant_id)

        except Error as error:
            raise error
