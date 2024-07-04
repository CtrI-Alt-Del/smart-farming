from core.use_cases.plants import UpdateActivePlant
from infra.repositories import plants_repository, users_repository


class UpdateActivePlantFactory:
    @staticmethod
    def produce():
        return UpdateActivePlant(
            plants_repository=plants_repository, users_repository=users_repository
        )
