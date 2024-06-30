from core.use_cases.plants import CreatePlantByForm
from infra.repositories import plants_repository, users_repository


class CreatePlantByFormFactory:
    @staticmethod
    def produce():
        return CreatePlantByForm(
            users_repository=users_repository, plants_repository=plants_repository
        )
