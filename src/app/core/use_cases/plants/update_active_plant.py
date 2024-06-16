from core.commons import Error

from infra.repositories import users_repository


class UpdateActivePlant:
    def execute(self, user_id: str, plant_id: str):
        try:
            if not isinstance(user_id, str):
                raise Error(ui_message="Usuário inválido")

            if not isinstance(plant_id, str):
                raise Error(ui_message="Planta inválida")

            users_repository.update_active_plant(user_id, plant_id)
        except Error as error:
            raise error
