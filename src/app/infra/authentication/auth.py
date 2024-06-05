from typing import Callable
from dataclasses import asdict
from functools import wraps

from flask_login import login_user, logout_user, login_required
from flask_bcrypt import Bcrypt


from core.entities import User
from infra.repositories import users_repository

from .auth_user import AuthUser


class Auth:
    def __init__(self, bcrypt: Bcrypt) -> None:
        self.bcrypt = bcrypt

    def load_user(self, user_id: str) -> AuthUser:
        id = user_id

        user = users_repository.get_user_by_id(id)

        if user is None:
            return AuthUser(is_active=False)

        return AuthUser(is_active=True, **asdict(user))

    def login(self, user: User, should_remember_user: bool):
        auth_user = AuthUser(**asdict(user))

        return login_user(auth_user, remember=should_remember_user)

    def logout(self):
        return logout_user()

    def login_middleware(self, view: Callable):
        @wraps(view)
        def check_login(*args, **kwargs):
            return login_required(view)(*args, **kwargs)

        return check_login

    def check_password(self, password_hash: str, password: str):
        return self.bcrypt.check_password_hash(password_hash, password)

    def generate_hash(self, text: str):
        return self.bcrypt.generate_password_hash(text).decode("utf-8")
