from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


def check_password(password_hash: str, password) -> bool:
    return bcrypt.check_password_hash(password_hash, password)
