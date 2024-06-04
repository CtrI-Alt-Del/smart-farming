from dataclasses import asdict

from .auth_user import AuthUser


def load_user(user_id: str) -> AuthUser:
    id = user_id

    user = users_repository.get_by_id(id)

    if user is None:
        return AuthUser(is_active=False)

    return AuthUser(is_active=True, **asdict(user))
