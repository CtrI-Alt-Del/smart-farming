from core.commons import Error
from core.constants import ADMIN_USER_EMAIL

from infra.repositories import users_repository
from infra.authentication import auth


class ResetPassword:
    def execute(self, new_password: str):
        try:
            password_hash = auth.generate_hash(new_password)

            users_repository.update_password(
                email=ADMIN_USER_EMAIL, new_password=password_hash
            )

        except Error as error:
            raise error
