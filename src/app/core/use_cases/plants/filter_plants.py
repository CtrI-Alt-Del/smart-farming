from core.interfaces.repositories import (
    PlantsRepositoryInterface,
)
from core.errors.plants import PlantNameNotValidError


class FilterPlants:
    def __init__(
        self,
        repository: PlantsRepositoryInterface,
    ):
        self.repository = repository

    def execute(self, plant_name: str | None):
        if not isinstance(plant_name, str):
            raise PlantNameNotValidError()

        plant_name = plant_name.strip()

        if len(plant_name) != 0:
            return self.repository.filter_plants_by_name(plant_name)

        return self.repository.get_plants()
