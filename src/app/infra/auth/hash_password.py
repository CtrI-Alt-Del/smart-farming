from flask_bcrypt import Bcrypt
from flask import render_template_string

bcrypt = Bcrypt()


def hash_password(password: str) -> bytes:
    render_template_string("", token="")
    return bcrypt.generate_password_hash(password).decode("utf-8")
