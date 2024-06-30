from core.use_cases.plants import DeletePlant
from infra.repositories import plants_repository, users_repository


class DeletePlantFactory:
    @staticmethod
    def produce():
        return DeletePlant(
            users_repository=users_repository, plants_repository=plants_repository
        )
