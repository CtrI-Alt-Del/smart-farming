from core.errors.authentication import NewPasswordNotValidError
from core.interfaces.repositories import UsersRepositoryInterface
from core.interfaces.authentication import AuthInterface
from core.constants import ADMIN_USER_EMAIL


class ResetPassword:
    def __init__(
        self,
        repository: UsersRepositoryInterface,
        auth: AuthInterface,
    ):
        self._repository = repository
        self._auth = auth

    def execute(self, new_password: str):
        if not isinstance(new_password, str):
            raise NewPasswordNotValidError()

        password_hash = self._auth.generate_hash(new_password)

        self._repository.update_password(
            email=ADMIN_USER_EMAIL, new_password=password_hash
        )
