from core.commons import Error

from core.entities import User
from core.constants import SUPPORT_USER_EMAIL

from infra.authentication import auth
from infra.repositories import users_repository


class LoginUser:
    def execute(self, email: str, password: str, should_remember_user: bool):
        try:
            if email != SUPPORT_USER_EMAIL:
                raise Error("E-mail ou senha incorretos", status_code=400)

            user = users_repository.get_user_by_email(email)

            if not isinstance(user, User):
                raise Error("Usuário não encontrado", status_code=500)

            is_password_correct = auth.check_hash(user.password, password)

            if not is_password_correct:
                raise Error("E-mail ou senha incorretos", status_code=400)

            is_login_success = auth.login(user, should_remember_user)

            if not is_login_success:
                raise Error("E-mail ou senha incorretos", status_code=400)

        except Error as error:
            raise error
