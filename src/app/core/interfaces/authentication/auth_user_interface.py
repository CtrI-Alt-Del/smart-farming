from abc import ABC, abstractmethod

from core.entities import User


class AuthUserInterface(User, ABC):
    is_active: bool = True

    @abstractmethod
    def get_id(self) -> str: ...

    @property
    def is_authenticated(self) -> bool: ...
