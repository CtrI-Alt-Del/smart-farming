from core.commons import Error
from infra.repositories import user_repository


class GetUserById:
    def execute(self, id: str) -> None:
        try:
            if not isinstance(id, str):
                raise Error("Usuário não encontrado", status_code=404)

            user = user_repository.get_user_by_id(id)
            return user

        except Error as error:
            raise error
