from core.commons import Error

from infra.repositories import plants_repository


class DeletePlant:
    def execute(self, id: str) -> None:
        try:
            if not isinstance(id, str):
                raise Error(
                    ui_message="Planta não encontrada",
                    internal_message="Plant id not provided",
                    status_code=404,
                )

            has_plant = bool(plants_repository.get_plant_by_id(id))

            if not has_plant:
                raise Error(
                    ui_message="Planta não encontrado",
                    internal_message="Plant not found",
                    status_code=404,
                )

            plants_repository.delete_plant_by_id(id)

        except Error as error:
            raise error
