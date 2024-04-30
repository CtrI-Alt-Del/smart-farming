from core.commons import Error
from core.entities import Plant
from infra.repositories import plants_repository


class UpdatePlants:
    def execute(self, request: dict) -> None:
        try:
            plants_id = request["plants_id"]

            if not plants_id or not isinstance(plants_id, str):
                raise Error(
                    ui_message="Registro plant não encontrado",
                    internal_message="Plant id not found",
                )

            has_plants = bool(
                plants_repository.get_plant_by_id(
                    plants_id
                )
            )

            if not has_plants:
                raise Error(
                    ui_message="Registro plant não encontrado",
                    internal_message="Plant record id not found",
                )

            plant = Plant(
                id=plants_id,
                name=request["name"],
                hex_color=request["hex_color"],
                
            )

            plants_repository.update_plant_by_id(plant)

        except Error as error:
            raise error
