from core.use_cases.plants import GetPlantsPageData
from infra.repositories import plants_repository


class GetPlantsPageDataFactory:
    @staticmethod
    def produce():
        return GetPlantsPageData(plants_repository)
