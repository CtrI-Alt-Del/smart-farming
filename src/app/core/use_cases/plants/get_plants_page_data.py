from core.interfaces.repositories import (
    PlantsRepositoryInterface,
)


class GetPlantsPageData:
    def __init__(
        self,
        repository: PlantsRepositoryInterface,
    ):
        self.repository = repository

    def execute(self):
        plants = self.repository.get_plants()

        return plants
