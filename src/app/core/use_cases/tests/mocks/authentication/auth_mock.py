from core.entities import User


class AuthMock:
    _user = None
    _should_remember_user: bool = False

    def get_user(self):
        return self._user

    def login(self, user: User, should_remember_user: bool):
        self._user = user
        self._should_remember_user = should_remember_user

        return True

    def logout(self):
        self._user = None

    def check_hash(self, hash: str, text: str) -> bool:
        return True

    def generate_hash(self, text: str) -> str:
        return text

    @property
    def should_remember_user(self):
        return self._should_remember_user
