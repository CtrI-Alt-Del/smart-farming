from core.entities import User
from core.interfaces.repositories import UsersRepositoryInterface

from infra.database import mysql


class UsersRepository(UsersRepositoryInterface):
    def get_user_by_id(
        self, id: str, should_include_password: bool = False
    ) -> User | None:
        row = mysql.query(
            sql="SELECT * FROM user WHERE id = %s",
            params=[id],
            is_single=True,
        )

        if row:
            user = self.__get_user_entity(row)

            if not should_include_password:
                del user.password

            return user

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

    def get_user_active_plant_id(self, email: str) -> User | None:
        row = mysql.query(
            sql="SELECT active_plant_id FROM user WHERE email = %s",
            params=[email],
            is_single=True,
        )

        return row["active_plant_id"] if row else None

    def update_password(self, email, new_password: str):
        mysql.mutate(
            """
            UPDATE user SET password = %s WHERE email = %s
            """,
            params=[new_password, email],
        )

    def update_active_plant(self, id: str, plant_id: str):
        mysql.mutate(
            """
            UPDATE user SET active_plant_id = %s WHERE id = %s
            """,
            params=[plant_id, id],
        )

    def __get_user_entity(self, row):
        return User(
            id=row["id"],
            email=row["email"],
            password=row["password"],
            active_plant_id=row["active_plant_id"],
        )
