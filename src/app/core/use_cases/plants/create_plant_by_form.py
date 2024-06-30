from core.entities.plant import Plant
from core.commons import Error
from core.interfaces.repositories import PlantsRepositoryInterface


class CreatePlantByForm:
    def __init__(self, plants_repository: PlantsRepositoryInterface):
        self.plants_repository = plants_repository

    def execute(self, request: dict):
        try:
            has_plant = self.plants_repository.get_plant_by_name(request["name"])

            if has_plant:
                raise Error("Nome de planta já utilizada")

            plant = Plant(name=request["name"], hex_color=request["hex_color"])

            self.plants_repository.create_plant(plant)

        except Error as error:
            raise error
