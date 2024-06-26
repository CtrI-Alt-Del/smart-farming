from core.commons import Error, Plant

from infra.repositories import users_repository, plants_repository


class UpdateActivePlant:
    def execute(self, user_id: str, plant_id: str):
        try:
            if not isinstance(user_id, str):
                raise Error(ui_message="Usuário inválido", status_code=400)

            if not isinstance(plant_id, str):
                raise Error(ui_message="Planta inválida", status_code=400)

            plant = plants_repository.get_plant_by_id(plant_id)

            if not isinstance(plant, Plant):
                raise Error(ui_message="Planta não encontrada", status_code=404)

            users_repository.update_active_plant(user_id, plant_id)
        except Error as error:
            raise error
