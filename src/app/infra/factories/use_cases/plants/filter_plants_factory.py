from core.use_cases.plants import FilterPlants
from infra.repositories import plants_repository


class FilterPlantsFactory:
    @staticmethod
    def produce():
        return FilterPlants(plants_repository)
