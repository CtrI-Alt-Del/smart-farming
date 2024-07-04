from core.use_cases.plants import GetPlantById
from infra.repositories import plants_repository


class GetPlantByIdFactory:
    @staticmethod
    def produce():
        return GetPlantById(plants_repository)
