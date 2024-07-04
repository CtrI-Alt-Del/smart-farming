from core.entities import User
from core.errors.authentication import CredentialsNotValidError, UserNotFoundError
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
        if email != ADMIN_USER_EMAIL:
            raise CredentialsNotValidError()

        user = self._repository.get_user_by_email(ADMIN_USER_EMAIL)

        if not isinstance(user, User):
            raise UserNotFoundError()

        is_password_correct = self._auth.check_hash(user.password, password)

        if not is_password_correct:
            raise CredentialsNotValidError()

        is_login_success = self._auth.login(user, should_remember_user)

        if not is_login_success:
            raise CredentialsNotValidError()
