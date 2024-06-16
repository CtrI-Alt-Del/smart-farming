from dataclasses import dataclass

from .entity import Entity


@dataclass
class User(Entity):
    email: str = None
    password: str = None
    active_plant_id: str = None
