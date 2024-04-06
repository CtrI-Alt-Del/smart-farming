from dataclasses import dataclass
from datetime import datetime

from entities.entity import Entity

@dataclass
class Sensors(Entity):
    soil_humidity: int = None
    ambient_humidity: int = None
    temperature: int = None
    water_volume: int = None
    created_at: datetime = None