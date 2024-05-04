from core.commons import Error
from core.entities import Plant
from infra.repositories import plants_repository


class UpdatePlant:
    def execute(self, request: dict, id: str) -> None:
        try:
            if not id or not isinstance(id, str):
                raise Error(
                    ui_message="Planta não encontrada",
                    internal_message="Plant id not provided",
                    status_code=404,
                )

            has_plant = bool(plants_repository.get_plant_by_id(id))

            if not has_plant:
                raise Error(
                    ui_message="Planta não encontrada",
                    internal_message="Plant not found",
                    status_code=404,
                )

            plant = Plant(
                id=id,
                name=request["name"],
                hex_color=request["hex_color"],
            )

            plants_repository.update_plant_by_id(plant)

            return plant

        except Error as error:
            raise error
