from core.commons import Error
from core.entities import User
from core.interfaces.repositories import UsersRepositoryInterface
from core.interfaces.authentication import AuthInterface
from core.constants import ADMIN_USER_EMAIL


class LoginUser:
    def __init__(
        self,
        repository: UsersRepositoryInterface,
        auth: AuthInterface,
    ):
        self._repository = repository
        self._auth = auth

    def execute(self, email: str, password: str, should_remember_user: bool):
        try:
            if email != ADMIN_USER_EMAIL:
                raise Error("E-mail ou senha incorretos", status_code=401)

            user = self._repository.get_user_by_email(ADMIN_USER_EMAIL)

            if not isinstance(user, User):
                raise Error("Usuário não encontrado", status_code=500)

            is_password_correct = self._auth.check_hash(user.password, password)

            if not is_password_correct:
                raise Error("E-mail ou senha incorretos", status_code=401)

            is_login_success = self._auth.login(user, should_remember_user)

            if not is_login_success:
                raise Error("E-mail ou senha incorretos", status_code=401)

        except Error as error:
            raise error
