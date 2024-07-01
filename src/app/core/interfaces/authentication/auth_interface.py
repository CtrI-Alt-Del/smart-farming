from abc import ABC, abstractmethod

from core.entities import User

from .auth_user_interface import AuthUserInterface


class AuthInterface(ABC):
    @abstractmethod
    def get_user(self) -> AuthUserInterface: ...

    @abstractmethod
    def load_user(self, user_id: str) -> AuthUserInterface: ...

    @abstractmethod
    def login(self, user: User, should_remember_user: bool) -> AuthUserInterface: ...

    @abstractmethod
    def logout(self) -> None: ...

    @abstractmethod
    def check_hash(self, hash: str, text: str) -> bool: ...

    @abstractmethod
    def generate_hash(self, text: str) -> str: ...
