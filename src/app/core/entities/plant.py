from dataclasses import dataclass

from .entity import Entity


@dataclass
class Plant(Entity):
    name: str = None
    hex_color: str = None
