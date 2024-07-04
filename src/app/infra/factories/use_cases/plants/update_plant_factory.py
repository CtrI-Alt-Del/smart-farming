from core.use_cases.plants import UpdatePlant
from infra.repositories import plants_repository


class UpdatePlantFactory:
    @staticmethod
    def produce():
        return UpdatePlant(plants_repository)
