from core.entities.plant import Plant
from core.commons import Error
from infra.repositories import plants_repository


class CreatePlantByForm:
    def execute(self, request: dict):
        try:
            has_plant = plants_repository.get_plant_by_name(request["name"])

            if has_plant:
                raise Error("Nome de planta já utilizada")

            plant = Plant(name=request["name"], hex_color=request["hex_color"])

            plants_repository.create_plant_record(plant)

        except Error as error:
            raise error
