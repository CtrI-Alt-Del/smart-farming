from core.entities.plant import Plant
from core.commons import Error
from infra.repositories import plants_repository


class CreatePlantByForm:
    def execute(self, request: dict) -> None:

        try:
            plant = Plant(
                name = request["name"],
                hex_color = request["hex_color"]
            )

            plants_repository.create_plants_record(plant)

        except Error as error:
            raise error