from core.entities.plant import Plant
from core.interfaces.repositories import PlantsRepositoryInterface
from core.errors.plants import PlantNameAlreadyInUseError


class CreatePlantByForm:
    def __init__(self, plants_repository: PlantsRepositoryInterface):
        self.plants_repository = plants_repository

    def execute(self, request: dict):
        has_plant = self.plants_repository.get_plant_by_name(request["name"])

        if has_plant:
            raise PlantNameAlreadyInUseError()

        plant = Plant(name=request["name"], hex_color=request["hex_color"])

        self.plants_repository.create_plant(plant)
