from flask_bcrypt import Bcrypt


class Password:
    def __init__(self, bcrypt: Bcrypt) -> None:
        self.bcrypt = bcrypt

    def hash_password(self, password: str) -> bytes:
        return self.bcrypt.generate_password_hash(password).decode("utf-8")
