from core.commons import Error
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
        try:
            if not isinstance(new_password, str):
                raise Error(
                    "Nova senha não fornecida",
                    internal_message="New password is not provided",
                    status_code=400,
                )

            password_hash = self._auth.generate_hash(new_password)

            self._repository.update_password(
                email=ADMIN_USER_EMAIL, new_password=password_hash
            )

        except Error as error:
            raise error
