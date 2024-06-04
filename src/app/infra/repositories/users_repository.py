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
