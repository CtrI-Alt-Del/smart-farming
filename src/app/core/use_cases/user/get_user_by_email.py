from core.commons import Error
from infra.repositories import user_repository


class GetUserByEmail:
    def execute(self, email: str) -> None:
        try:
            if not isinstance(email, str):
                raise Error("Usuário não encontrado", status_code=404)

            user = user_repository.get_user_by_email(email)
            return user

        except Error as error:
            raise error
