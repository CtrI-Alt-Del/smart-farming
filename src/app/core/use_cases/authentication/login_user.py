from core.commons import Error
from core.entities import User
from core.constants import SUPPORT_USER_EMAIL

from infra.authentication import auth
from infra.repositories import users_repository


class LoginUser:
    def execute(self, email: str, should_remember_user: bool):
        try:
            if email != SUPPORT_USER_EMAIL:
                raise Error("E-mail ou senha incorretos", status_code=400)

            user = users_repository.get_user_by_email(email)

            if not isinstance(user, User):
                raise Error("Usuário não encontrado", status_code=500)

            auth.login(user, should_remember_user)

        except Error as error:
            raise error
