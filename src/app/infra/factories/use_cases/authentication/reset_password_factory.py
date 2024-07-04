from core.use_cases.authentication import ResetPassword

from infra.repositories import users_repository
from infra.authentication import auth


class ResetPasswordFactory:
    @staticmethod
    def produce():
        return ResetPassword(repository=users_repository, auth=auth)
