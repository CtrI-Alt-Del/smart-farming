from core.entities import User
from core.interfaces.repositories import UsersRepositoryInterface


class UsersRepositoryMock(UsersRepositoryInterface):
    _users: list[User] = []

    def get_user_by_id(self, id: str) -> User | None:
        users = list(filter(lambda user: user.id == id, self._users))

        if len(users):
            return users[0]

        return None

    def get_user_by_email(self, email: str) -> User | None:
        users = list(filter(lambda user: user.email == email, self._users))

        if len(users):
            return users[0]

        return None

    def get_user_active_plant_id(self, email: str) -> User | None:
        user = self.get_user_by_email(email)

        return user.active_plant_id if user else None

    def update_password(self, email, new_password: str):
        user = self.get_user_by_email(email)

        user.password = new_password

        self.__update_user(user)

    def update_active_plant(self, id: str, plant_id: str):
        user = self.get_user_by_id(id)

        user.active_plant_id = plant_id

        self.__update_user(user)

    def create_user(self, user: User):
        self._users.append(user)

    def __update_user(self, user):
        self._users = [
            current_user if current_user.id != user.id else user
            for current_user in self._users
        ]
