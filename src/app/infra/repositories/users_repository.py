from core.entities import User
from infra.database import mysql


class UsersRepository:
    def get_user_by_id(self, id: str) -> User | None:
        row = mysql.query(
            sql="SELECT * FROM user WHERE id = %s",
            params=[id],
            is_single=True,
        )

        if row:
            return self.__get_user_entity(row)

        return None

    def update_password(self, user_id: str, new_password: str) -> User | None:
        print(user_id,flush=True)
        print(new_password,flush=True)
        mysql.mutate(
            """
        UPDATE user SET password = %s WHERE id = %s
        """,
            params=[new_password, user_id],
        )
        

    def get_user_by_email(self, email: str) -> User | None:
        row = mysql.query(
            sql="SELECT * FROM user WHERE email = %s",
            params=[email],
            is_single=True,
        )

        if row:
            return self.__get_user_entity(row)

        return None

    def __get_user_entity(self, row):
        return User(id=row["id"], email=row["email"], password=row["password"])
