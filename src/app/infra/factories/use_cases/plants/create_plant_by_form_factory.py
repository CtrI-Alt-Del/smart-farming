from core.use_cases.plants import CreatePlantByForm
from infra.repositories import plants_repository


class CreatePlantByFormFactory:
    @staticmethod
    def produce():
        return CreatePlantByForm(plants_repository=plants_repository)
