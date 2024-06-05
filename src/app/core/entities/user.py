from dataclasses import dataclass

from core.entities.entity import Entity


@dataclass
class User(Entity):
    email: str = None
    password: str = None
