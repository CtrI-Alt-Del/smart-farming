from dataclasses import dataclass

from core.entities import User


@dataclass
class AuthUser(User):
    is_active: bool = True

    def get_id(self) -> str:
        return self.id

    @property
    def is_authenticated(self):
        return self.is_active
