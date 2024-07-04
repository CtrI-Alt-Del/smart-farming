from core.interfaces.repositories import (
    PlantsRepositoryInterface,
)
from core.errors.plants import PlantIdNotValidError


class GetPlantById:
    def __init__(
        self,
        repository: PlantsRepositoryInterface,
    ):
        self.repository = repository

    def execute(self, id: str):
        if not isinstance(id, str):
            raise PlantIdNotValidError()

        return self.repository.get_plant_by_id(id)
