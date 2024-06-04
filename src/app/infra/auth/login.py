from flask_login import login_user

from core.entities import User


def login(user: User, should_remember_user: bool):
    return login_user(user, remember=should_remember_user)
