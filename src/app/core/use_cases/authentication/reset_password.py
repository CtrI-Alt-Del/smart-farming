
from core.commons import Error

from infra.repositories import users_repository



class ResetPassword:
    def execute(self, user_id: str,new_password: str):
        try:
            users_repository.update_password(user_id=user_id,new_password=new_password)

        except Error as error:
            raise Error(ui_message=error, internal_message=error)
