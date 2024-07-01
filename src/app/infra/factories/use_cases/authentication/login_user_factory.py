from core.use_cases.authentication import LoginUser

from infra.repositories import users_repository
from infra.authentication import auth


class LoginUserFactory:
    @staticmethod
    def produce():
        return LoginUser(repository=users_repository, auth=auth)
